
window.APP = {
    data: null,
    router: null,
    fuse: null,

    async init() {
        if (!window.KB_DATA) {
            console.error("Data not loaded");
            return;
        }

        this.data = window.KB_DATA;
        this.router = new window.Router(this.data);

        // Init Search
        this.fuse = new Fuse(this.data.index, {
            keys: ['title', 'content'],
            threshold: 0.3,
            ignoreLocation: true
        });

        // initial Render
        this.renderSidebar(this.data.tree, document.getElementById('nav-tree'));
        this.bindEvents();
        this.initEffects();
    },

    initEffects() {
        // 1. Spotlight Mouse Tracking
        document.addEventListener('mousemove', (e) => {
            document.documentElement.style.setProperty('--mouse-x', `${e.clientX}px`);
            document.documentElement.style.setProperty('--mouse-y', `${e.clientY}px`);
        });

        // 2. Scroll Observer for Content Boxes
        // We attach this to a global window property so Router can use it
        window.contentObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    // Stop observing once visible to save performance
                    window.contentObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '50px'
        });
    },

    bindEvents() {
        // Mobile Toggle
        const toggle = document.getElementById('menu-toggle');
        const sidebar = document.getElementById('sidebar');

        toggle.addEventListener('click', () => {
            // Check if mobile or desktop based on window width
            if (window.innerWidth <= 768) {
                sidebar.classList.toggle('visible');
            } else {
                document.querySelector('.app-layout').classList.toggle('collapsed');
            }
        });

        // Search
        const searchInput = document.getElementById('searchInput');
        const results = document.getElementById('searchResults');

        searchInput.addEventListener('input', (e) => {
            const query = e.target.value;
            if (!query) {
                results.classList.add('hidden');
                return;
            }

            const hits = this.fuse.search(query).slice(0, 10);
            if (hits.length === 0) {
                results.innerHTML = '<div style="padding:10px; color:#888;">No results</div>';
            } else {
                results.innerHTML = hits.map(h => `
                    <div class="result-item" data-path="${h.item.path}">
                        <div style="font-weight:bold">${h.item.title}</div>
                        <div style="font-size:0.8em; opacity:0.6">${h.item.path}</div>
                    </div>
                `).join('');

                results.querySelectorAll('.result-item').forEach(el => {
                    el.onclick = () => {
                        window.location.hash = el.dataset.path;
                        results.classList.add('hidden');
                        if (window.innerWidth <= 768) sidebar.classList.remove('visible');
                    };
                });
            }
            results.classList.remove('hidden');
        });
    },

    renderSidebar(node, container, currentPath = '') {
        // Sort: Folders first, then files
        const entries = Object.entries(node).sort((a, b) => {
            const aIsFile = a[1].type === 'file';
            const bIsFile = b[1].type === 'file';
            if (aIsFile !== bIsFile) return aIsFile ? 1 : -1;
            return a[0].localeCompare(b[0]);
        });

        entries.forEach(([name, item]) => {
            if (item.type === 'file') {
                const el = document.createElement('a');
                el.className = 'nav-link';
                el.href = `#${item.path}`;
                el.innerText = name.replace(item.ext, '').replace(/_/g, ' ');
                container.appendChild(el);
            } else {
                // Folder Path
                const itemPath = currentPath ? `${currentPath}/${name}` : name;

                const group = document.createElement('div');
                group.className = 'nav-group';

                const header = document.createElement('div');
                header.className = 'nav-header';
                // Add data-path for router highlighting if needed
                header.setAttribute('data-path', itemPath);

                header.innerHTML = `<span class="icon">▶</span> <span>${name.replace(/_/g, ' ')}</span>`;

                header.onclick = (e) => {
                    e.stopPropagation();
                    // Navigate to folder view
                    window.location.hash = itemPath;
                    // Standard behavior: Toggle expansion when clicking folder
                    group.classList.toggle('open');
                };

                const children = document.createElement('div');
                children.className = 'nav-children';

                group.appendChild(header);
                group.appendChild(children);
                container.appendChild(group);

                this.renderSidebar(item, children, itemPath);
            }
        });
    }
};

window.navigateTo = function (path) {
    window.location.hash = path;
};

document.addEventListener('DOMContentLoaded', () => window.APP.init());
