 // Initialize roadmap functionality
        document.addEventListener('DOMContentLoaded', function() {
            const nodes = document.querySelectorAll('.roadmap-node');
            const checkboxes = document.querySelectorAll('.node-checkbox');
            const progressFill = document.getElementById('progressFill');
            const progressText = document.getElementById('progressText');
            const totalNodes = nodes.length;
            let completedNodes = 0;

            // Determine roadmap type from the h1 tag's data attribute
            const roadmapTypeElement = document.querySelector('h1[data-roadmap-type]');
            const roadmapType = roadmapTypeElement ? roadmapTypeElement.dataset.roadmapType : 'default'; // Fallback to 'default'

            // Create floating particles
            createFloatingParticles();

            // Animate roadmap paths on load
            setTimeout(() => {
                document.querySelectorAll('.roadmap-path').forEach((path, index) => {
                    setTimeout(() => {
                        path.classList.add('animated');
                    }, index * 100);
                });
            }, 500);

            // Load progress from local storage
            loadProgress();
            updateProgress();

            // Add click functionality to nodes (for expanding content)
            nodes.forEach((node, index) => {
                node.addEventListener('click', function(e) {
                    // Don't expand if clicking on checkbox
                    if (e.target.closest('.custom-checkbox')) return;

                    const contentArea = node.querySelector('.content-area');
                    const isExpanded = contentArea.classList.contains('expanded');

                    // Close other expanded nodes
                    nodes.forEach(otherNode => {
                        if (otherNode !== node) {
                            otherNode.querySelector('.content-area').classList.remove('expanded');
                        }
                    });

                    // Toggle current node's content
                    contentArea.classList.toggle('expanded', !isExpanded);
                });

                // Add change listener to checkboxes
                const checkbox = node.querySelector('.node-checkbox');
                if (checkbox) {
                    checkbox.addEventListener('change', function() {
                        node.classList.toggle('completed', this.checked);
                        updateProgress();
                        saveProgress();
                    });
                }
            });

            function updateProgress() {
                completedNodes = 0;
                checkboxes.forEach(checkbox => {
                    if (checkbox.checked) {
                        completedNodes++;
                    }
                });

                const progressPercentage = (completedNodes / totalNodes) * 100;
                progressFill.style.width = `${progressPercentage}%`;
                progressText.textContent = `${completedNodes}/${totalNodes}`;
            }

            function saveProgress() {
                const progress = {};
                checkboxes.forEach((checkbox, index) => {
                    progress[index] = checkbox.checked;
                });
                // Use a unique key based on roadmapType
                localStorage.setItem(`${roadmapType}RoadmapProgress`, JSON.stringify(progress));
            }

            function loadProgress() {
                // Load from the unique key
                const savedProgress = localStorage.getItem(`${roadmapType}RoadmapProgress`);
                if (savedProgress) {
                    const progress = JSON.parse(savedProgress);
                    checkboxes.forEach((checkbox, index) => {
                        if (progress[index]) {
                            checkbox.checked = true;
                            checkbox.closest('.roadmap-node').classList.add('completed');
                        }
                    });
                }
            }

            function createFloatingParticles() {
                const particlesContainer = document.getElementById('particles');
                const numberOfParticles = 30; // Adjust as needed

                for (let i = 0; i < numberOfParticles; i++) {
                    const particle = document.createElement('div');
                    particle.classList.add('particle');
                    particle.style.width = `${Math.random() * 5 + 5}px`; /* 5 to 10px */
                    particle.style.height = particle.style.width;
                    particle.style.left = `${Math.random() * 100}vw`;
                    particle.style.animationDuration = `${Math.random() * 5 + 5}s`; // 5 to 10 seconds
                    particle.style.animationDelay = `${Math.random() * 6}s`; // Stagger animation start
                    particlesContainer.appendChild(particle);
                }
            }
        });