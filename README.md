# Worfux - Frappe + Vue 3 + Frappe UI Starter App

This template should help get you started developing custom frontend for Frappe
apps with Vue 3 and the Frappe UI package.

![Auth](https://user-images.githubusercontent.com/34810212/236846289-ac31c292-81ea-4456-be65-95773a4049be.png)

![Home](https://user-images.githubusercontent.com/34810212/236846299-fd534e2b-1c06-4f01-a4f2-91a27547cd55.png)

This boilerplate sets up Vue 3, Vue Router, TailwindCSS, and Frappe UI out of
the box. It also has basic authentication frontend.

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
