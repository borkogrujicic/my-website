# PROJECT.md - Project-Specific Customizations

> **Purpose:** This file contains YOUR project-specific customizations and preferences.
> **Priority:** Instructions here **override** the defaults in `AGENTS.md`.
> **AI Agents:** All coding assistants (Claude Code, Cursor, Copilot, Windsurf, etc.) read this file with **highest priority**.

**Why PROJECT.md?**
- **Clear name:** Immediately signals "project-specific instructions"
- **Universal:** Works with ALL AI coding assistants, not just one tool
- **Hierarchical:** Higher priority than AGENTS.md (which contains defaults)

---

## 🎨 Design Customizations

### Colors
<!-- Uncomment and customize to override AstroDeck's default color scheme -->

<!-- Example: Change primary color from blue to vibrant purple
```css
:root {
  --primary: 270 91% 65%;              /* Vibrant purple instead of blue */
  --primary-foreground: 0 0% 100%;
}
```
-->

<!-- Example: Custom brand colors
```css
:root {
  --primary: 215 100% 50%;             /* Your brand blue */
  --accent: 45 93% 58%;                /* Your brand yellow */
  --background: 0 0% 100%;             /* Pure white background */
}
```
-->

### Typography
<!-- Uncomment and customize fonts -->

<!-- Example: Use custom Google Fonts
Add to your layout:
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

Then in globals.css:
```css
body {
  font-family: 'Inter', sans-serif;
}
```
-->

---

## ✍️ Content Guidelines

### Tone of Voice
<!-- Define how content should be written -->

<!-- Example:
- **Style:** Professional but friendly, conversational
- **Audience:** Tech-savvy startup founders and developers
- **Language:** US English, avoid jargon unless necessary
- **Personality:** Helpful, confident, slightly playful
-->

### Brand Voice
<!-- Example:
- ✅ DO: Use "we" and "our" (inclusive language)
- ✅ DO: Write in active voice
- ❌ DON'T: Use corporate buzzwords or marketing fluff
- ❌ DON'T: Make unverifiable claims
-->

---

## 🚀 Project-Specific Rules

### Component Preferences
<!-- Example: Always use specific patterns for your project -->

<!-- Example:
- All forms must include Zod validation
- All API calls must use the `useQuery` hook from TanStack Query
- All images must use Astro's <Image /> component with alt text
-->

### File Naming
<!-- Example: Enforce specific naming conventions -->

<!-- Example:
- API routes: Use kebab-case (e.g., `get-user-profile.ts`)
- React components: Use PascalCase with `.tsx` extension
- Utility functions: Use camelCase with `.ts` extension
-->

---

## 📝 Custom Commands

### Shortcuts
<!-- Define custom workflows that AI should follow -->

<!-- Example:
When I say "add a new section":
1. Create component in `src/components/sections/`
2. Follow the Section Component Template from AGENTS.md
3. Add TypeScript Props interface
4. Include mobile-responsive design
5. Test in both light and dark mode
-->

### Project-Specific Workflows
<!-- Example:
When deploying:
1. Run `npm run build` to verify production build
2. Check Lighthouse scores (must be >90 for all metrics)
3. Test on mobile device
4. Update CHANGELOG.md
5. Create git tag with version number
-->

---

## 🎯 Business Context

### Project Goals
<!-- Help AI understand your project's purpose -->

<!-- Example:
This is a SaaS landing page for "YourProduct" - an AI-powered analytics tool for e-commerce.
Target audience: Small to medium-sized online retailers (Shopify, WooCommerce users)
Key differentiator: Real-time inventory predictions using machine learning
-->

### Key Features to Emphasize
<!-- What should stand out in the design/copy? -->

<!-- Example:
1. Real-time dashboard (hero feature)
2. Predictive analytics (main value prop)
3. Easy Shopify integration (reduce friction)
4. Free trial with no credit card (conversion focus)
-->

---

## 🔧 Technical Preferences

### Code Style
<!-- Project-specific coding preferences beyond AGENTS.md -->

<!-- Example:
- Prefer functional components over class components
- Use early returns to reduce nesting
- Prefer explicit over implicit (e.g., always use curly braces for if statements)
- Maximum line length: 100 characters
-->

### Dependencies
<!-- Preferences for libraries and tools -->

<!-- Example:
- ✅ PREFER: Native Web APIs over libraries when possible
- ✅ PREFER: Astro components over React for static content
- ❌ AVOID: Adding new dependencies without discussion
- ❌ AVOID: Using deprecated npm packages
-->

---

## 💡 Example: Override Primary Color

**Scenario:** Change AstroDeck's default blue primary color to a vibrant electric blue.

**Step 1:** Update `src/styles/globals.css`
```css
@layer base {
  :root {
    --primary: 212 100% 48%;              /* Electric blue (#0066FF) */
    --primary-foreground: 0 0% 100%;      /* White text on blue */
  }
}
```

**Step 2:** Tell AI agents in this file:
```markdown
## Design Customizations

### Primary Color
Our brand color is **electric blue** (#0066FF).
- Use this for all CTAs, links, and primary actions
- Maintain WCAG AA contrast ratio (4.5:1 minimum)
- Test in both light and dark mode
```

**Result:** All AI-generated code will now use electric blue instead of the default AstroDeck blue.

---

## 📚 Additional Resources

<!-- Link to relevant docs, style guides, brand assets -->

<!-- Example:
- Brand Guidelines: [link to Figma/Google Drive]
- Content Style Guide: [link to Notion/Confluence]
- API Documentation: [link to your API docs]
- Design System: [link to Storybook/Figma]
-->

---

**Remember:** This file is YOUR project context. The more specific you are, the better AI agents can help you build exactly what you need.
