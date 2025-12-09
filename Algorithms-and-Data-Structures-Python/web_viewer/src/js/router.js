
window.Router = class Router {
    constructor(data) {
        this.data = data;

        window.addEventListener('hashchange', () => this.handleRoute());

        // Initial load
        if (window.location.hash) {
            this.handleRoute();
        } else {
            this.renderHome();
        }
    }

    handleRoute() {
        let hash = window.location.hash.slice(1);
        console.log(`Router: Handling route. Hash raw: "${window.location.hash}", Parsed: "${hash}"`);
        try { hash = decodeURIComponent(hash); } catch (e) { console.error("Router: Decode failed", e); }

        // 1. Sidebar Active State
        document.querySelectorAll('.nav-link').forEach(el => el.classList.remove('active'));

        if (!hash) {
            this.renderHome();
            return;
        }

        // --- Sidebar highlighting ---
        // --- Sidebar highlighting ---
        // Try to find a File Link first
        let activeEl = document.querySelector(`.nav-link[href="#${CSS.escape(hash)}"]`) ||
            document.querySelector(`.nav-link[href="#${hash}"]`);

        // If not a file, try to find a Folder Header
        if (!activeEl) {
            const cleanHash = hash.replace(/\/$/, ''); // Remove trailing slash if any
            activeEl = document.querySelector(`.nav-header[data-path="${CSS.escape(cleanHash)}"]`) ||
                document.querySelector(`.nav-header[data-path="${cleanHash}"]`);
        }

        if (activeEl) {
            // If it's a folder header, maybe mark it active or just open parents?
            // Let's mark it active for visual feedback
            activeEl.classList.add('active'); // CSS might need to style .nav-header.active

            let parent = activeEl.parentElement; // .nav-group if it's a header, or container if root?

            // If it's a header, its parent is a nav-group. We want to open THIS group?
            // "inside mathematics folder... button not open their folders"
            // If I am AT "Mathematics", I probably want to see its children in sidebar?
            // If activeEl is a header, it's inside a .nav-group.

            // Walk up to open PARENTS - REMOVED per user request
            // User wants NO sidebar expansion on navigation

            // Just mark active
            activeEl.classList.add('active');
        }

        // 2. Resolve Path
        const node = this.resolvePath(hash);

        if (!node) {
            this.renderHome();
        } else if (node.type === 'file') {
            const indexItem = this.data.index.find(i => i.path === hash);
            if (indexItem) this.renderPage(indexItem);
            else {
                this.renderPage({
                    title: hash.split('/').pop(),
                    content: node.content,
                    type: 'Content',
                    breadcrumbs: hash.split('/').slice(0, -1),
                    path: hash
                });
            }
        } else {
            this.renderFolderView(node, hash);
        }
    }

    resolvePath(pathString) {
        if (!pathString) return this.data.tree;
        const parts = pathString.split('/').filter(p => p);
        let current = this.data.tree;

        for (const part of parts) {
            if (current && current[part]) {
                current = current[part];
            } else {
                return null;
            }
        }
        return current;
    }

    renderHome() {
        this.renderFolderView(this.data.tree, '');
    }

    renderFolderView(node, currentPath) {
        const contentEl = document.getElementById('content');

        // Helper: Count items
        const countItems = (n) => {
            let count = 0;
            if (n.type === 'file') return 1;
            for (const key in n) {
                if (n[key].type === 'file') count++;
                else count += countItems(n[key]);
            }
            return count;
        };

        let gridHtml = '';

        // "Back" Card if not root
        if (currentPath) {
            const parentPath = currentPath.split('/').slice(0, -1).join('/');
            gridHtml += `
                <a class="topic-card back-card" href="#${parentPath}">
                    <div class="card-icon-svg">
                        <svg viewBox="0 0 100 100" class="svg-icon back-icon">
                            <defs>
                                <linearGradient id="backGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                                    <stop offset="0%" style="stop-color:#444;stop-opacity:1" />
                                    <stop offset="100%" style="stop-color:#222;stop-opacity:1" />
                                </linearGradient>
                            </defs>
                            <!-- Back Plate -->
                            <path d="M10,35 L40,35 L50,45 L90,45 C92.76,45 95,47.24 95,50 L95,85 C95,87.76 92.76,90 90,90 L10,90 C7.24,90 5,87.76 5,85 L5,40 C5,37.24 7.24,35 10,35 Z" fill="url(#backGrad)" opacity="0.6" />
                            <!-- Arrow UP -->
                             <path d="M50,70 L50,30 M30,50 L50,30 L70,50" fill="none" stroke="#00ff41" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" filter="drop-shadow(0 0 5px #00ff41)"/>
                        </svg>
                    </div>
                    <div class="card-title">Go Up</div>
                    <div class="card-meta">Parent Directory</div>
                </a>
            `;
        }

        // Sort: Folders first, then files
        const entries = Object.entries(node).sort((a, b) => {
            const aIsFile = a[1].type === 'file';
            const bIsFile = b[1].type === 'file';
            if (aIsFile !== bIsFile) return aIsFile ? 1 : -1;
            return a[0].localeCompare(b[0]);
        });

        entries.forEach(([key, item]) => {
            const itemPath = currentPath ? `${currentPath}/${key}` : key;
            const displayName = key.replace(/_/g, ' ');

            if (item.type !== 'file') {
                // PREMIUM 3D GLASS FOLDER ICON
                const folderIcon = `
                <svg viewBox="0 0 100 100" class="svg-icon folder-icon">
                    <defs>
                        <!-- Back Plate Gradient -->
                        <linearGradient id="backPlate" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#3a86ff;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#004e92;stop-opacity:1" />
                        </linearGradient>
                        <!-- Front Glass Gradient -->
                        <linearGradient id="frontGlass" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" style="stop-color:#7ccbf9;stop-opacity:0.9" />
                            <stop offset="50%" style="stop-color:#3a86ff;stop-opacity:0.85" />
                            <stop offset="100%" style="stop-color:#004e92;stop-opacity:0.9" />
                        </linearGradient>
                        <!-- Gloss Reflection -->
                        <linearGradient id="gloss" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" style="stop-color:#fff;stop-opacity:0.4" />
                            <stop offset="100%" style="stop-color:#fff;stop-opacity:0.1" />
                        </linearGradient>
                    </defs>
                    
                    <!-- File Papers hinting content inside -->
                    <rect x="20" y="25" width="60" height="50" rx="2" fill="#fff" fill-opacity="0.7" transform="rotate(-5 50 50)" />
                    <rect x="25" y="25" width="60" height="50" rx="2" fill="#fff" fill-opacity="0.9" filter="drop-shadow(0 2px 3px rgba(0,0,0,0.2))" />

                    <!-- Back Folder Tab -->
                    <path d="M10,35 L40,35 L50,45 L90,45 C92.76,45 95,47.24 95,50 L95,85 C95,87.76 92.76,90 90,90 L10,90 C7.24,90 5,87.76 5,85 L5,40 C5,37.24 7.24,35 10,35 Z" fill="url(#backPlate)" />

                    <!-- Front Glass Plate -->
                    <path d="M5,55 L15,45 L95,45 L95,85 C95,87.76 92.76,90 90,90 L10,90 C7.24,90 5,87.76 5,85 Z" fill="url(#frontGlass)" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
                    
                    <!-- Subtle Highlight on edge -->
                    <path d="M15,46 L94,46" stroke="url(#gloss)" stroke-width="2" stroke-linecap="round" />
                </svg>`;

                const count = countItems(item);
                gridHtml += `
                    <a class="topic-card folder-card" href="#${itemPath}">
                        <div class="card-icon-svg">${folderIcon}</div>
                        <div class="card-title">${displayName}</div>
                        <div class="card-meta">${count} items</div>
                    </a>
                `;
            } else {
                // PREMIUM FILE ICON
                let fileIcon = '';
                if (key.endsWith('.py')) {
                    // Python Icon
                    fileIcon = `
                    <svg viewBox="0 0 100 100" class="svg-icon file-icon python-icon">
                        <path d="M50,15 C40,15 35,20 35,25 L35,35 L55,35 L55,30 L65,30 L65,45 L45,45 L45,40 L25,40 L25,25 C25,10 40,5 50,5 C60,5 75,10 75,25 L75,35 L65,35 L65,25 C65,20 60,15 50,15 Z" fill="#3776ab"/>
                        <circle cx="42" cy="22" r="3" fill="#fff"/>
                        <path d="M50,85 C60,85 65,80 65,75 L65,65 L45,65 L45,70 L35,70 L35,55 L55,55 L55,60 L75,60 L75,75 C75,90 60,95 50,95 C40,95 25,90 25,75 L25,65 L35,65 L35,75 C35,80 40,85 50,85 Z" fill="#ffd343"/>
                        <circle cx="58" cy="78" r="3" fill="#fff"/>
                    </svg>`;
                } else if (key.endsWith('.md')) {
                    // Markdown/Text Icon
                    fileIcon = `
                    <svg viewBox="0 0 100 100" class="svg-icon file-icon md-icon">
                        <path d="M20,10 L60,10 L80,30 L80,90 C80,92.76 77.76,95 75,95 L25,95 C22.24,95 20,92.76 20,90 L20,10 Z" fill="#f0f0f0" stroke="#ccc" stroke-width="1"/>
                        <path d="M60,10 L60,30 L80,30" fill="#ddd" />
                        <path d="M35,40 L35,60 L42,50 L49,60 L49,40" fill="none" stroke="#333" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M65,40 L60,60 H70 L65,40" fill="none" stroke="#333" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                        <line x1="30" y1="75" x2="70" y2="75" stroke="#aaa" stroke-width="2"/>
                        <line x1="30" y1="82" x2="60" y2="82" stroke="#aaa" stroke-width="2"/>
                    </svg>`;
                } else {
                    // Generic File
                    fileIcon = `
                     <svg viewBox="0 0 100 100" class="svg-icon file-icon">
                        <path d="M20,10 L60,10 L80,30 L80,90 C80,92.76 77.76,95 75,95 L25,95 C22.24,95 20,92.76 20,90 L20,10 Z" fill="#fff" stroke="#999" stroke-width="1"/>
                        <path d="M60,10 L60,30 L80,30" fill="#eee" />
                    </svg>`;
                }

                gridHtml += `
                    <a class="topic-card file-card" href="#${itemPath}">
                        <div class="card-icon-svg">${fileIcon}</div>
                        <div class="card-title">${displayName.replace('.md', '').replace('.py', '')}</div>
                    </a>
                `;
            }
        });

        const title = currentPath ? currentPath.split('/').pop().replace(/_/g, ' ') : 'Agorithms & Data Structures';
        const subtitle = currentPath
            ? currentPath.split('/').map(p => p.replace(/_/g, ' ')).join(' / ')
            : 'A comprehensive knowledge base for Computer Science, implemented in Python.';

        const html = `
            <div class="hero-section">
                <div class="hero-title">${title}</div>
                <div class="hero-subtitle">${subtitle}</div>
            </div>
            <div class="topic-grid">
                ${gridHtml}
            </div>
        `;

        contentEl.innerHTML = html;

        // Update top bar breadcrumbs
        let crumbHtml = `<a class="crumb-link" href="#">Home</a>`;
        if (currentPath) {
            const parts = currentPath.split('/');
            let buildPath = '';
            parts.forEach(part => {
                buildPath += (buildPath ? '/' : '') + part;
                crumbHtml += `<span class="sep">/</span><a class="crumb-link" href="#${buildPath}">${part.replace(/_/g, ' ')}</a>`;
            });
        }
        document.getElementById('breadcrumbs').innerHTML = crumbHtml;

        document.getElementById('content-scroll').scrollTop = 0;
    }

    renderPage(item) {
        const contentEl = document.getElementById('content');

        // Update Breadcrumbs
        const crumbsEl = document.getElementById('breadcrumbs');
        let crumbHtml = `<a class="crumb-link" href="#">Home</a>`;

        const parts = item.path.split('/');
        parts.pop(); // Remove file

        let buildPath = '';
        parts.forEach(part => {
            buildPath += (buildPath ? '/' : '') + part;
            crumbHtml += `<span class="sep">/</span><a class="crumb-link" href="#${buildPath}">${part.replace(/_/g, ' ')}</a>`;
        });

        // Add current page title (non-clickable)
        crumbHtml += `<span class="sep">/</span><span class="crumb-current">${item.title}</span>`;
        crumbsEl.innerHTML = crumbHtml;

        let html = '';
        if (item.type === 'Code' || item.path.endsWith('.py')) {
            const container = document.createElement('div');
            container.className = 'content-box title-box'; // Style as a main box

            const h1 = document.createElement('h1');
            h1.innerText = item.title;

            const pre = document.createElement('pre');
            const code = document.createElement('code');
            code.className = 'language-python';
            code.textContent = item.content; // textContent preserves \n unlike innerText
            code.style.whiteSpace = 'pre'; // Force inline to be 100% sure

            pre.appendChild(code);
            container.appendChild(h1);
            container.appendChild(pre);

            contentEl.innerHTML = '';
            contentEl.appendChild(container);

            // CRITICAL: Observe it so it becomes visible
            if (window.contentObserver) window.contentObserver.observe(container);
            else container.classList.add('visible'); // Fallback if observer missing
        } else {
            // New "Boxed" Rendering Logic
            const rawHtml = marked.parse(item.content);
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = rawHtml;

            const finalContainer = document.createElement('div');
            finalContainer.className = 'boxed-content';

            let currentBox = null;

            Array.from(tempDiv.children).forEach(child => {
                // Determine if we should start a new box
                // H1 starts the main Intro box
                // H2 starts a new Major Section box
                const isHeader = ['H1', 'H2'].includes(child.tagName);

                if (isHeader || !currentBox) {
                    currentBox = document.createElement('section');
                    currentBox.className = 'content-box';
                    // Check if it's the main title box
                    if (child.tagName === 'H1') currentBox.classList.add('title-box');

                    // Add staggere animation delay
                    // const index = finalContainer.children.length; // REMOVED: Using Observer now
                    // currentBox.style.animationDelay = `${index * 0.1}s`; 

                    finalContainer.appendChild(currentBox);

                    // Observe for scroll effect
                    if (window.contentObserver) window.contentObserver.observe(currentBox);
                }
                currentBox.appendChild(child);
            });

            contentEl.innerHTML = '';
            contentEl.appendChild(finalContainer);
        }

        hljs.highlightAll();
        if (window.MathJax) MathJax.typesetPromise([contentEl]);

        document.getElementById('content-scroll').scrollTop = 0;

        if (window.innerWidth <= 768) {
            document.getElementById('sidebar').classList.remove('visible');
        }
    }

    escapeHtml(text) {
        return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }
};
