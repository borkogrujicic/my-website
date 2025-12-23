# AI Developer Guide

**👋 Welcome, AI Assistant!**

This guide is specifically designed to help you (AI coding assistants like Claude, ChatGPT, Cursor, Copilot, etc.) understand AstroDeck and provide better assistance to developers.

---

## 🎯 Quick Context

**What is AstroDeck?**
An open-source component library for Astro.js that provides pre-built, copy-paste ready sections for building landing pages and SaaS websites quickly.

**Core Purpose:**
Help developers ship beautiful websites faster by providing production-ready components they can customize.

**Target Users:**
- Web developers building landing pages
- SaaS founders creating marketing sites
- Agencies building client websites
- Indie hackers launching products

---

## 🏗️ Architecture Overview

### Technology Stack

```
┌─────────────────────────────────────┐
│         Astro (latest)              │  ← Framework (island architecture)
├─────────────────────────────────────┤
│       Tailwind CSS (latest)         │  ← Styling (utility-first)
├─────────────────────────────────────┤
│    shadcn/ui + Radix UI             │  ← UI Components (React)
├─────────────────────────────────────┤
│         TypeScript (latest)         │  ← Type Safety
└─────────────────────────────────────┘
```

### Why This Stack?

**Astro:**
- Zero-JS by default = blazing fast
- Island architecture = interactive components only where needed
- File-based routing = intuitive page creation
- Works with React, Vue, Svelte (we use React for shadcn/ui)

**Tailwind CSS:**
- Rapid prototyping with utility classes
- No CSS conflicts or naming issues
- Easy theme customization via CSS variables
- Excellent responsive design workflow

**shadcn/ui:**
- Beautiful, accessible components
- Copy-paste approach (code is in the project, not npm)
- Built on Radix UI primitives
- Fully customizable with Tailwind

### Project Structure

```
astrodeck/
├── src/
│   ├── components/
│   │   ├── sections/          ← Pre-built page sections
│   │   │   ├── Hero.astro     ← Homepage hero
│   │   │   ├── CTA.astro      ← Call-to-action
│   │   │   ├── Features.astro ← Feature showcase
│   │   │   ├── Pricing.astro  ← Pricing table
│   │   │   ├── Testimonials.astro
│   │   │   ├── LogoCloud.astro
│   │   │   └── ContentBlock.astro
│   │   ├── ui/                ← shadcn/ui components
│   │   │   ├── button.tsx     ← React components
│   │   │   ├── card.tsx
│   │   │   ├── badge.tsx
│   │   │   └── input.tsx
│   │   ├── Header.astro       ← Site header
│   │   ├── Footer.astro       ← Site footer
│   │   └── ThemeToggle.astro  ← Dark mode toggle
│   ├── layouts/               ← Page templates
│   │   ├── BaseLayout.astro   ← Default (boxed, max-w-5xl)
│   │   ├── FullWidthLayout.astro ← Full width
│   │   └── AuthLayout.astro   ← No header/footer
│   ├── pages/                 ← File-based routing
│   │   ├── index.astro        ← / (homepage)
│   │   ├── sections.astro     ← /sections (component library)
│   │   ├── login.astro        ← /login
│   │   └── privacy.astro      ← /privacy
│   ├── styles/
│   │   └── globals.css        ← Global styles + CSS variables
│   └── lib/
│       └── utils.ts           ← Helper functions
└── public/                    ← Static assets
    └── fonts/                 ← Web fonts
```

---

## 🎨 Design System

### Theme System

AstroDeck uses CSS variables for theming, enabling easy light/dark mode switching.

**Color Variables (in `src/styles/globals.css`):**

```css
:root {
  --background: 0 0% 100%;        /* White */
  --foreground: 222 47% 11%;      /* Dark text */
  --primary: 221 83% 53%;         /* Primary color */
  --primary-foreground: 0 0% 100%; /* White on primary */
  --muted: 210 40% 96%;           /* Muted backgrounds */
  --muted-foreground: 215 16% 47%; /* Muted text */
  /* ... more variables */
}

.dark {
  --background: 222 47% 11%;      /* Dark background */
  --foreground: 0 0% 100%;        /* Light text */
  /* ... dark mode overrides */
}
```

**How to Use in Components:**

```astro
<!-- ✅ Correct: Use semantic color classes -->
<div class="bg-background text-foreground">
<button class="bg-primary text-primary-foreground">
<p class="text-muted-foreground">

<!-- ❌ Wrong: Don't hardcode colors -->
<div class="bg-white text-black">      <!-- Breaks dark mode -->
<button class="bg-blue-500 text-white"> <!-- Ignores theme -->
```

### Responsive Breakpoints

```
sm:  640px   - Small tablets
md:  768px   - Tablets
lg:  1024px  - Small laptops
xl:  1280px  - Desktops
2xl: 1536px  - Large screens
```

**Always use mobile-first:**

```astro
<!-- ✅ Mobile-first approach -->
<h1 class="text-3xl md:text-5xl lg:text-6xl">

<!-- ❌ Don't do this -->
<h1 class="text-6xl lg:text-3xl">
```

---

## 📝 Common Development Tasks

### Task 1: Create a New Page

**Steps:**
1. Create file in `src/pages/`
2. Choose appropriate layout
3. Add sections
4. File name = URL route

**Example: Create an "About" page**

```astro
---
// src/pages/about.astro
import BaseLayout from "@/layouts/BaseLayout.astro";
import Hero from "@/components/sections/Hero.astro";
import Features from "@/components/sections/Features.astro";
---

<BaseLayout
  title="About Us"
  description="Learn about our mission and team"
>
  <Hero />
  <Features />
</BaseLayout>
```

**Result:** Page available at `/about`

### Task 2: Create a New Section Component

**Steps:**
1. Create file in `src/components/sections/`
2. Use semantic HTML
3. Make responsive with Tailwind
4. Support dark mode with CSS variables

**Example: Create a "Newsletter" section**

```astro
---
// src/components/sections/Newsletter.astro
interface Props {
  title?: string;
  description?: string;
}

const {
  title = "Subscribe to our newsletter",
  description = "Get the latest updates delivered to your inbox."
} = Astro.props;
---

<section class="py-20 px-6 bg-muted/30">
  <div class="max-w-3xl mx-auto text-center">
    <h2 class="text-3xl font-bold mb-4">{title}</h2>
    <p class="text-muted-foreground mb-8">{description}</p>

    <form class="flex gap-2 max-w-md mx-auto">
      <input
        type="email"
        placeholder="your@email.com"
        class="flex-1 h-12 rounded-md border px-4 text-sm bg-background"
      />
      <button class="h-12 px-6 bg-primary text-primary-foreground rounded-md font-medium hover:bg-primary/90">
        Subscribe
      </button>
    </form>
  </div>
</section>
```

### Task 3: Customize Theme Colors

**Steps:**
1. Open `src/styles/globals.css`
2. Edit CSS variables
3. Changes apply to both light and dark mode

**Example: Change primary color to green**

```css
/* src/styles/globals.css */
:root {
  --primary: 142 76% 36%;         /* Green instead of blue */
  --primary-foreground: 0 0% 100%;
}
```

**Don't edit `tailwind.config.mjs` for colors!** This breaks the theme system.

### Task 4: Add an Interactive Component

**When to use:**
- Forms that need validation
- Modals/dialogs
- Dropdowns with state
- Anything requiring client-side JS

**Example: Add a contact form**

```astro
---
// src/pages/contact.astro
import BaseLayout from "@/layouts/BaseLayout.astro";
import ContactForm from "@/components/ContactForm.tsx";
---

<BaseLayout title="Contact Us">
  <div class="py-20 px-6">
    <div class="max-w-2xl mx-auto">
      <h1 class="text-4xl font-bold mb-8">Get in Touch</h1>
      <ContactForm client:load />
    </div>
  </div>
</BaseLayout>
```

```tsx
// src/components/ContactForm.tsx
import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

export default function ContactForm() {
  const [email, setEmail] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Handle form submission
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <Input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Your email"
      />
      <Button type="submit">Send Message</Button>
    </form>
  );
}
```

---

## 🧩 Component Patterns

### Section Component Anatomy

All section components follow this pattern:

```astro
---
// 1. Props interface (optional but recommended)
interface Props {
  title?: string;
  subtitle?: string;
  variant?: 'default' | 'centered' | 'wide';
}

// 2. Destructure props with defaults
const {
  title = "Default Title",
  subtitle,
  variant = 'default'
} = Astro.props;
---

<!-- 3. Semantic HTML wrapper -->
<section class="py-20 px-6">

  <!-- 4. Container for width constraint -->
  <div class="max-w-7xl mx-auto">

    <!-- 5. Content structure -->
    <div class="text-center mb-12">
      <h2 class="text-4xl font-bold mb-4">{title}</h2>
      {subtitle && (
        <p class="text-lg text-muted-foreground">{subtitle}</p>
      )}
    </div>

    <!-- 6. Main content -->
    <div class="grid md:grid-cols-3 gap-8">
      <!-- Content goes here -->
    </div>

  </div>
</section>
```

### Layout Selection Guide

**BaseLayout** - Use for most pages
```astro
<BaseLayout title="Page Title" description="SEO description">
  <!-- Content is centered with max-w-5xl -->
</BaseLayout>
```
**When:** Blog posts, documentation, content pages

**FullWidthLayout** - Use for showcase pages
```astro
<FullWidthLayout title="Components" description="Browse components">
  <!-- Content spans full viewport width -->
</FullWidthLayout>
```
**When:** Component libraries, portfolios, galleries

**AuthLayout** - Use for authentication
```astro
<AuthLayout title="Login">
  <!-- No header/footer, centered content -->
</AuthLayout>
```
**When:** Login, signup, password reset pages

---

## 🚨 Common Pitfalls & How to Avoid

### Pitfall 1: Hardcoded Colors

❌ **Wrong:**
```astro
<div class="bg-blue-500 text-white">
```

✅ **Correct:**
```astro
<div class="bg-primary text-primary-foreground">
```

**Why:** Hardcoded colors break dark mode and theme customization.

### Pitfall 2: Inline Styles

❌ **Wrong:**
```astro
<div style="padding: 80px; background: #f5f5f5;">
```

✅ **Correct:**
```astro
<div class="py-20 bg-muted">
```

**Why:** Inline styles can't be themed and break the utility-first approach.

### Pitfall 3: Relative Imports

❌ **Wrong:**
```astro
import Hero from "../components/sections/Hero.astro";
```

✅ **Correct:**
```astro
import Hero from "@/components/sections/Hero.astro";
```

**Why:** `@/` alias is cleaner and works from any file depth.

### Pitfall 4: Creating .tsx for Static Content

❌ **Wrong:**
```tsx
// HeroSection.tsx - Don't do this for static content
export default function HeroSection() {
  return <section>...</section>;
}
```

✅ **Correct:**
```astro
<!-- Hero.astro - Use Astro for static sections -->
<section>...</section>
```

**Why:** Astro components ship zero JS by default. React adds unnecessary bundle size.

### Pitfall 5: Ignoring Responsive Design

❌ **Wrong:**
```astro
<h1 class="text-6xl">Title</h1>
```

✅ **Correct:**
```astro
<h1 class="text-3xl md:text-5xl lg:text-6xl">Title</h1>
```

**Why:** Large text on mobile creates poor UX.

---

## 🎯 AI Assistant Guidelines

### When Generating Code

1. **Always use TypeScript** - Add proper type annotations
2. **Follow mobile-first** - Start with mobile, scale up with breakpoints
3. **Use semantic HTML** - `<section>`, `<article>`, `<nav>`, `<header>`, `<footer>`
4. **Think accessibility** - Add ARIA labels, alt text, proper heading hierarchy
5. **Keep it simple** - Don't over-engineer, follow existing patterns
6. **Comment wisely** - Explain *why*, not *what*

### When Debugging

Check these first:
1. ✓ Using `@/` import alias?
2. ✓ Using CSS variable classes (bg-primary, not bg-blue-500)?
3. ✓ Layout imported and used correctly?
4. ✓ TypeScript types defined for props?
5. ✓ Component responsive on mobile?
6. ✓ Works in dark mode?

### When Refactoring

1. **Maintain patterns** - Don't introduce new patterns without good reason
2. **Test after changes** - Ensure dev server still works
3. **Keep scope small** - Refactor one thing at a time
4. **Document changes** - Add comments explaining architectural decisions

### Code Quality Checklist

Before suggesting code, verify:

- [ ] Uses `@/` imports
- [ ] Only Tailwind classes (no inline styles)
- [ ] Uses CSS variables for colors
- [ ] Mobile-responsive (uses breakpoints)
- [ ] TypeScript types for props
- [ ] Semantic HTML elements
- [ ] Works in light and dark mode
- [ ] Follows existing component patterns
- [ ] Accessible (ARIA, alt text, etc.)
- [ ] No unnecessary client-side JS

---

## 📚 Quick Reference

### Import Patterns

```astro
// Layouts
import BaseLayout from "@/layouts/BaseLayout.astro";
import FullWidthLayout from "@/layouts/FullWidthLayout.astro";
import AuthLayout from "@/layouts/AuthLayout.astro";

// Sections
import Hero from "@/components/sections/Hero.astro";
import CTA from "@/components/sections/CTA.astro";
import Features from "@/components/sections/Features.astro";
import Pricing from "@/components/sections/Pricing.astro";

// UI Components
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

// Utilities
import { cn } from "@/lib/utils"; // Class name merger
```

### Useful Tailwind Patterns

```astro
<!-- Container with max width -->
<div class="max-w-7xl mx-auto px-6">

<!-- Responsive grid -->
<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">

<!-- Centered content -->
<div class="flex items-center justify-center min-h-screen">

<!-- Card with hover effect -->
<div class="rounded-lg border bg-card p-6 hover:shadow-lg transition-shadow">

<!-- Button group -->
<div class="flex flex-col sm:flex-row gap-4">
```

### NPM Scripts

```bash
npm run dev      # Start dev server (http://localhost:4321)
npm run build    # Build for production (outputs to dist/)
npm run preview  # Preview production build locally
```

---

## 🤝 Best Practices for Helping Developers

### Understand the Intent

When a developer asks for help:
1. Clarify what they want to achieve
2. Suggest the simplest solution first
3. Follow AstroDeck patterns, don't introduce new ones
4. Provide code that's ready to copy-paste

### Provide Complete Examples

❌ **Don't give fragments:**
```astro
<div class="container">
  <!-- Add your content here -->
```

✅ **Give working code:**
```astro
---
import BaseLayout from "@/layouts/BaseLayout.astro";
---

<BaseLayout title="Example">
  <div class="max-w-7xl mx-auto px-6 py-20">
    <h1 class="text-4xl font-bold">Working Example</h1>
  </div>
</BaseLayout>
```

### Explain Decisions

When suggesting approaches, explain why:

```astro
<!-- Use BaseLayout for content pages because:
     1. Provides consistent header/footer
     2. Centers content for readability
     3. Handles SEO meta tags automatically -->
<BaseLayout title="About">
```

---

## 🎓 Learning Resources

**For Developers (reference these when explaining concepts):**
- Astro Docs: https://docs.astro.build
- Tailwind Docs: https://tailwindcss.com/docs
- shadcn/ui: https://ui.shadcn.com
- Accessibility: https://www.w3.org/WAI/ARIA/apg/

**Project Files to Reference:**
- Component examples: `/sections` page in browser
- Theme variables: `src/styles/globals.css`
- Config: `astro.config.mjs`, `tailwind.config.mjs`

---

## 🎯 Summary: Your Role as an AI Assistant

You're helping developers build faster with AstroDeck. Your job is to:

1. **Understand** the project structure and conventions
2. **Generate** code that follows AstroDeck patterns
3. **Explain** why certain approaches are recommended
4. **Debug** with context about the architecture
5. **Educate** developers about best practices

**Golden Rule:** Keep it simple, follow the patterns, prioritize user experience.

---

**Happy coding! 🚀**

*Last updated: December 2024*
