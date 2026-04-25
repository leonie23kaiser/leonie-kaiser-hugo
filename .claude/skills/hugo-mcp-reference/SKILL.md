---
name: hugo-mcp-reference
description: Reference guide for available MCP servers in this Hugo project. Use when asked what MCP tools are available, how to use Playwright for Hugo page verification, or how to automate browser testing for the SuperLeague.TV website.
user-invocable: true
---

# MCP Servers Reference

Quick reference for **Model Context Protocol (MCP)** servers configured in this repo.

---

## Available MCP Servers

### 🎭 Playwright (Browser Automation & Testing)

**Type:** Stdio | **Priority:** ⭐⭐⭐ Essential

**Use for:**

- ✅ Take screenshots of Hugo pages
- ✅ Verify page rendering
- ✅ Test responsive design
- ✅ Inspect DOM elements
- ✅ Capture metrics (load time, paint, etc.)
- ✅ Automated visual testing

**Quick Usage:**

```
"Use Playwright to take a screenshot of localhost:1313/fighters/"
"Verify that the fighter portrait renders correctly"
"Check if the fight card VS layout is visible on the event page"
```

**Real Example:**

```javascript
// Verify fighter page
const screenshot = await playwright.takeScreenshot({
  url: 'http://localhost:1313/fighters/valon-basha/'
});

const element = await playwright.querySelector({
  url: 'http://localhost:1313/fighters/valon-basha/',
  selector: 'img.fighter-portrait'
});

if (element.visible) {
  console.log('✅ Fighter portrait visible');
}
```

**Lab:** [Lab: Using MCP Servers](../../labs/lab-using-mcp-servers.md)

---

### 🔧 Chrome DevTools

**Type:** Stdio | **Priority:** ⭐⭐ Advanced

**Use for:**

- Performance profiling
- Network inspection
- JavaScript debugging
- Memory analysis
- Code coverage
- FCP/LCP metrics

**Quick Usage:**

```
"Profile the performance of the class page"
"Check for JavaScript errors on localhost:1313"
"Analyze network requests on the homepage"
```

---

### 🐙 GitHub

**Type:** HTTP | **Priority:** ⭐⭐⭐ Essential

**Use for:**

- Create/update pull requests
- Manage issues
- Trigger GitHub Actions
- Check CI/CD status
- Read repo data

**Quick Usage:**

```
"Create a PR for the new class feature"
"Check the status of the latest GitHub Actions workflow"
"List all open issues in the repository"
```

---

### 🎨 Figma

**Type:** HTTP | **Priority:** ⭐⭐ Optional

**Use for:**

- Extract design components
- Get design tokens
- Pull design specifications
- Access brand assets

**Quick Usage:**

```
"Extract the brand color palette from Figma"
"Get the latest design spec for class cards"
```

---

### ☁️ Azure Deploy

**Type:** Stdio | **Priority:** ⭐ Deployment

**Use for:**

- Deploy to Azure Static Web Apps
- Configure Azure Container Apps
- Manage resources

**Quick Usage:**

```
"Deploy the Hugo site to Azure"
```

---

### 📚 Microsoft Learn

**Type:** HTTP | **Priority:** Reference

**Use for:**

- Access documentation
- Find learning modules
- Get code examples

**Quick Usage:**

```
"Show me the Microsoft Learn documentation for Azure Static Web Apps"
```

---

### 🧩 Context7

**Type:** HTTP | **Priority:** Reference

**Use for:**

- Knowledge graphs
- Semantic search
- Related information

---

### 🧠 WorkIQ

**Type:** Stdio | **Priority:** Optional

**Use for:**

- Team insights
- Productivity metrics

---

### 📐 Angular CLI

**Type:** Stdio | **Priority:** Optional (if using Angular)

**Use for:**

- Generate Angular components
- Build Angular projects
- Test Angular apps

---

## Top Use Cases for This Project

### ✅ Verify Fighter Page

```
"After adding a new fighter, use Playwright to verify it renders correctly at /fighters/[fighter-slug]/"
→ Takes screenshot, checks portrait, verifies fight record
```

### ✅ Verify Image Rendering

```
"Use Playwright to check that the fighter portrait appears on the profile page"
→ Confirms image file exists and displays correctly
```

### ✅ Debug Layout Issues

```
"Use Chrome DevTools to profile the fighters list page and show me the performance metrics"
→ Returns load time, FCP, LCP, rendering metrics
```

### ✅ Create Feature PRs

```
"Use GitHub to create a PR for the new event page feature"
→ Creates PR, adds description, ready for review
```

### ✅ Check CI/CD Status

```
"Use GitHub to check the status of the latest workflow run"
→ Shows if the Azure Static Web Apps deploy passed/failed
```
