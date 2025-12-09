
// Three.js Background Animation - "Knowledge Graph"
// Creates a subtle network of connected nodes floating in 3D space.

export function initVisuals() {
    const canvas = document.createElement('canvas');
    canvas.id = 'bg-canvas';
    document.body.prepend(canvas);

    if (!window.THREE) {
        console.warn('Three.js not loaded');
        return;
    }

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });

    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);

    // Particles
    const geometry = new THREE.BufferGeometry();
    const count = 150;
    const positions = new Float32Array(count * 3);
    const velocities = [];

    for (let i = 0; i < count * 3; i++) {
        positions[i] = (Math.random() - 0.5) * 20; // Spread
        if (i % 3 === 0) velocities.push({
            x: (Math.random() - 0.5) * 0.005,
            y: (Math.random() - 0.5) * 0.005,
            z: (Math.random() - 0.5) * 0.005
        });
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    // Material for Dots
    const material = new THREE.PointsMaterial({
        color: 0x3b82f6, // Blue
        size: 0.08,
        transparent: true,
        opacity: 0.6
    });

    const particles = new THREE.Points(geometry, material);
    scene.add(particles);

    // Lines (Connections)
    const lineMaterial = new THREE.LineBasicMaterial({
        color: 0x3b82f6,
        transparent: true,
        opacity: 0.15
    });

    const linesGeometry = new THREE.BufferGeometry();
    const lines = new THREE.LineSegments(linesGeometry, lineMaterial);
    scene.add(lines);

    camera.position.z = 5;

    // Mouse Interaction
    let mouseX = 0;
    let mouseY = 0;

    document.addEventListener('mousemove', (event) => {
        mouseX = (event.clientX / window.innerWidth) - 0.5;
        mouseY = (event.clientY / window.innerHeight) - 0.5;
    });

    // Animation Loop
    function animate() {
        requestAnimationFrame(animate);

        const posAttribute = geometry.attributes.position;
        const positions = posAttribute.array;

        // Update Particles
        for (let i = 0; i < count; i++) {
            positions[i * 3] += velocities[i].x;
            positions[i * 3 + 1] += velocities[i].y;
            positions[i * 3 + 2] += velocities[i].z;

            // Boundary Check (Loop around)
            if (positions[i * 3] > 10) positions[i * 3] = -10;
            if (positions[i * 3] < -10) positions[i * 3] = 10;
            if (positions[i * 3 + 1] > 10) positions[i * 3 + 1] = -10;
            if (positions[i * 3 + 1] < -10) positions[i * 3 + 1] = 10;
        }

        posAttribute.needsUpdate = true;

        // Update Camera (Parallax)
        camera.position.x += (mouseX * 2 - camera.position.x) * 0.05;
        camera.position.y += (-mouseY * 2 - camera.position.y) * 0.05;
        camera.lookAt(scene.position);

        // Update Lines (Connect close particles)
        const linePositions = [];
        const connectionDistance = 2.5;

        for (let i = 0; i < count; i++) {
            for (let j = i + 1; j < count; j++) {
                const dx = positions[i * 3] - positions[j * 3];
                const dy = positions[i * 3 + 1] - positions[j * 3 + 1];
                const dz = positions[i * 3 + 2] - positions[j * 3 + 2];
                const dist = Math.sqrt(dx * dx + dy * dy + dz * dz);

                if (dist < connectionDistance) {
                    linePositions.push(
                        positions[i * 3], positions[i * 3 + 1], positions[i * 3 + 2],
                        positions[j * 3], positions[j * 3 + 1], positions[j * 3 + 2]
                    );
                }
            }
        }

        linesGeometry.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));

        renderer.render(scene, camera);
    }

    animate();

    // Resize Handler
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
}
