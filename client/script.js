document.addEventListener('DOMContentLoaded', () => {
    const dashboardBtn = document.getElementById('dashboardBtn');
    const apiBtn = document.getElementById('apiBtn');
    const graphBtn = document.getElementById('graphBtn');
    const impactBtn = document.getElementById('impactBtn');
    const remediationBtn = document.getElementById('remediationBtn');
    const content = document.getElementById('content');

    dashboardBtn.addEventListener('click', async () => {
        content.innerHTML = '<h2>Dashboard Content</h2><p>Loading...</p>';
        try {
            const response = await fetch('http://localhost:8000/api/integrations/');
            if (!response.ok) throw new Error('Failed to fetch');
            const data = await response.json();
            
            let tableHTML = '<h2>Dashboard Content</h2><table border="1"><tr><th>ID</th><th>Name</th><th>Description</th></tr>';
            data.forEach(integration => {
                tableHTML += `<tr><td>${integration.id}</td><td>${integration.name}</td><td>${integration.description}</td></tr>`;
            });
            tableHTML += '</table>';
            content.innerHTML = tableHTML;
        } catch (error) {
            content.innerHTML = `<h2>Error</h2><p>${error.message}</p>`;
        }
    });

    apiBtn.addEventListener('click', async () => {
        content.innerHTML = '<h2>API Management</h2><p>Loading...</p>';
        try {
            const response = await fetch('http://localhost:8000/api/apis/');
            if (!response.ok) throw new Error('Failed to fetch');
            const data = await response.json();
            
            let tableHTML = '<h2>API Management</h2><table border="1"><tr><th>ID</th><th>Name</th><th>Endpoint</th></tr>';
            data.forEach(api => {
                tableHTML += `<tr><td>${api.id}</td><td>${api.name}</td><td>${api.endpoint}</td></tr>`;
            });
            tableHTML += '</table>';
            content.innerHTML = tableHTML;
        } catch (error) {
            content.innerHTML = `<h2>Error</h2><p>${error.message}</p>`;
        }
    });

    graphBtn.addEventListener('click', async () => {
        content.innerHTML = '<h2>Dependency Graph</h2><p>Loading...</p>';
        try {
            const response = await fetch('http://localhost:8000/api/graph/');
            if (!response.ok) throw new Error('Failed to fetch');
            const data = await response.json();
            content.innerHTML = `<h2>Dependency Graph</h2><pre>${JSON.stringify(data, null, 2)}</pre>`;
        } catch (error) {
            content.innerHTML = `<h2>Error</h2><p>${error.message}</p>`;
        }
    });

    impactBtn.addEventListener('click', async () => {
        content.innerHTML = '<h2>Impact Analysis</h2><p>Loading...</p>';
        try {
            const response = await fetch('http://localhost:8000/api/impact/');
            if (!response.ok) throw new Error('Failed to fetch');
            const data = await response.json();
            content.innerHTML = `<h2>Impact Analysis</h2><pre>${JSON.stringify(data, null, 2)}</pre>`;
        } catch (error) {
            content.innerHTML = `<h2>Error</h2><p>${error.message}</p>`;
        }
    });

    remediationBtn.addEventListener('click', async () => {
        content.innerHTML = '<h2>Remediation</h2><p>Loading...</p>';
        try {
            const response = await fetch('http://localhost:8000/api/remediation/');
            if (!response.ok) throw new Error('Failed to fetch');
            const data = await response.json();
            content.innerHTML = `<h2>Remediation</h2><pre>${JSON.stringify(data, null, 2)}</pre>`;
        } catch (error) {
            content.innerHTML = `<h2>Error</h2><p>${error.message}</p>`;
        }
    });

    // Load default content (dashboard)
    dashboardBtn.click();
});
