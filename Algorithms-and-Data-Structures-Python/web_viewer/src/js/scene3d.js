
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';

// V8: Cinematic Archive
// Circular Gallery with GSAP Animations and Bloom

let scene, camera, renderer, composer;
let interactables = [];
let raycaster, mouse;
let currentDirNode = null;
let navigationStack = [];
let routerInstance = null;
let isTransitioning = false;

// Config
const GALLERY_RADIUS = 15;

export function initScene(data, router) {
    routerInstance = router;
    currentDirNode = data.tree;

    const canvas = document.createElement('canvas');
    canvas.id = 'bg-canvas';
    document.body.prepend(canvas);

    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x020202);
    scene.fog = new THREE.FogExp2(0x020202, 0.02);

    camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 2, 35); // Initial view

    renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: false }); // Antialias off for Bloom perf
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.toneMapping = THREE.ReinhardToneMapping;

    // Post-Processing (Bloom)
    const renderScene = new RenderPass(scene, camera);
    const bloomPass = new UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 1.5, 0.4, 0.85);
    bloomPass.threshold = 0.1;
    bloomPass.strength = 1.2; // Glow strength
    bloomPass.radius = 0.5;

    composer = new EffectComposer(renderer);
    composer.addPass(renderScene);
    composer.addPass(bloomPass);

    // Lights
    const ambientLight = new THREE.AmbientLight(0x404040);
    scene.add(ambientLight);

    // Dynamic Spotlight following camera? Or fixed cinematic lights?
    const spotLight = new THREE.SpotLight(0xffffff, 500);
    spotLight.position.set(0, 20, 20);
    spotLight.angle = Math.PI / 4;
    spotLight.penumbra = 0.5;
    scene.add(spotLight);

    // Floor (Reflection)
    const floorGeo = new THREE.PlaneGeometry(200, 200);
    const floorMat = new THREE.MeshStandardMaterial({
        color: 0x050505, roughness: 0.1, metalness: 0.8
    });
    const floor = new THREE.Mesh(floorGeo, floorMat);
    floor.rotation.x = -Math.PI / 2;
    floor.position.y = -5;
    scene.add(floor);

    // Initial Render
    renderGallery(currentDirNode);

    // Interaction
    raycaster = new THREE.Raycaster();
    mouse = new THREE.Vector2();

    window.addEventListener('resize', onWindowResize);
    window.addEventListener('mousemove', onMouseMove);
    window.addEventListener('click', onMouseClick);
    window.goBack = goUpDirectory;

    animate();
}

function renderGallery(node) {
    // Clear old
    interactables.forEach(o => scene.remove(o));
    interactables = [];

    const entries = Object.entries(node);
    const count = entries.length;
    const angleStep = (Math.PI * 0.8) / Math.max(count, 1); // Spread over 140 degrees
    const startAngle = -((count - 1) * angleStep) / 2;

    entries.forEach(([name, item], index) => {
        const angle = startAngle + index * angleStep;
        const x = Math.sin(angle) * GALLERY_RADIUS;
        const z = Math.cos(angle) * GALLERY_RADIUS - 10; // Curving away

        createMonolith(name, item, new THREE.Vector3(x, 0, z), angle);
    });

    updateBreadcrumbs();
}

function createMonolith(name, item, pos, angle) {
    const isFolder = item.type !== 'file';

    // Geometry: Tall Monoliths for folders, shorter for files
    const h = isFolder ? 6 : 4;
    const w = 3;
    const d = 0.5;
    const geometry = new THREE.BoxGeometry(w, h, d);

    // Material: Glassy with Emissive edges
    const material = new THREE.MeshPhysicalMaterial({
        color: isFolder ? 0x111111 : 0x001100,
        metalness: 0.2,
        roughness: 0.1,
        transmission: 0.6,
        thickness: 2.0,
        emissive: isFolder ? 0x000000 : 0x002200,
    });

    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.copy(pos);
    mesh.rotation.y = angle; // Face center

    // Glowing Borders (The "Tron" lines)
    const edges = new THREE.EdgesGeometry(geometry);
    const lineMat = new THREE.LineBasicMaterial({ color: 0x00ff41 });
    const wireframe = new THREE.LineSegments(edges, lineMat);
    mesh.add(wireframe);

    mesh.userData = {
        name: name,
        item: item,
        isFolder: isFolder,
        basePos: pos.clone(),
        baseRot: angle
    };

    scene.add(mesh);
    interactables.push(mesh);

    // Animate In (Pop up)
    mesh.position.y -= 10;
    gsap.to(mesh.position, { duration: 1, y: pos.y, ease: "power3.out", delay: Math.random() * 0.3 });
}

function onMouseClick(event) {
    if (isTransitioning) return;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(interactables);

    if (intersects.length > 0) {
        const obj = intersects[0].object;

        if (obj.userData.isFolder) {
            enterFolder(obj);
        } else {
            openFile(obj);
        }
    }
}

function enterFolder(obj) {
    isTransitioning = true;

    // Cinematic Zoom into the folder
    const targetPos = obj.position.clone().add(new THREE.Vector3(0, 0, 5)); // Stop in front

    gsap.to(camera.position, {
        duration: 1.2,
        x: targetPos.x,
        y: targetPos.y,
        z: targetPos.z,
        ease: "power2.inOut",
        onComplete: () => {
            // Load new level
            navigationStack.push(currentDirNode);
            currentDirNode = obj.userData.item;
            renderGallery(currentDirNode);

            // Reset Camera
            camera.position.set(0, 2, 45); // Fly back out for broad view
            gsap.to(camera.position, { duration: 1.5, z: 35, ease: "power2.out" });
            isTransitioning = false;
        }
    });
}

function openFile(obj) {
    // Just trigger Router, no scene transition needed (Modal opens)
    window.location.hash = obj.userData.item.path;
}

function goUpDirectory() {
    if (navigationStack.length === 0 || isTransitioning) return;
    isTransitioning = true;

    // Fly Backwards
    gsap.to(camera.position, {
        duration: 0.5,
        z: camera.position.z + 20,
        opacity: 0,
        onComplete: () => {
            currentDirNode = navigationStack.pop();
            renderGallery(currentDirNode);

            // Zoom back in
            camera.position.z = 80;
            gsap.to(camera.position, { duration: 1.0, z: 35, ease: "power2.out" });
            isTransitioning = false;
        }
    });
}

function updateBreadcrumbs() {
    const container = document.getElementById('nav-controls');
    if (navigationStack.length > 0) {
        container.innerHTML = `<button class="back-btn" onclick="window.goBack()">←</button>`;
    } else {
        container.innerHTML = '';
    }
}

function onMouseMove(event) {
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
}

function animate() {
    requestAnimationFrame(animate);

    if (!isTransitioning) {
        // Subtle Camera float
        camera.position.x += (mouse.x * 2 - camera.position.x) * 0.02;
        camera.position.y += (mouse.y * 1 + 2 - camera.position.y) * 0.02;
        camera.lookAt(0, 0, 0);
    }

    // Hover Effects
    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(interactables);

    interactables.forEach(obj => {
        if (intersects.length > 0 && intersects[0].object === obj) {
            document.body.style.cursor = 'pointer';
            // Pop out
            gsap.to(obj.scale, { duration: 0.3, x: 1.1, y: 1.1, z: 1.1 });
        } else {
            gsap.to(obj.scale, { duration: 0.3, x: 1, y: 1, z: 1 });
        }
    });

    composer.render();
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
    composer.setSize(window.innerWidth, window.innerHeight);
}
