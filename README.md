# Worfux - Frappe + Vue 3 + Frappe UI Starter App

![Alt Text](https://github.com/1byZero/worfux/blob/main/worfux/public/ver1/img/macbook.webp)


This template should help get you started developing custom frontend for Frappe using this custom app with Vue 3 and the Frappe UI package.

## Usage

In your bench directory:

```
bench get-app https://github.com/1byZero/worfux.git
bench --site [site-name] install-app worfux

cd apps/worfux
Begin installing Worfix UI Starter App
```

In a development environment, you need to put the below key-value pair in your `site_config.json` file:

```
"ignore_csrf": 1
```

## Resources

- [Vue 3](https://v3.vuejs.org/guide/introduction.html)
- [Vue Router](https://next.router.vuejs.org/guide/)
- [Frappe UI](https://github.com/frappe/frappe-ui)
- [TailwindCSS](https://tailwindcss.com/docs/utility-first)
- [Vite](https://vitejs.dev/guide/)
