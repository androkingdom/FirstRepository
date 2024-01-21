# Taildwind Production Level Installation


**INSTALL TAILDWIND**

```
npm install -D tailwindcss
npx tailwindcss init
```

**EDIT *tailwind.config.js***

```
module.exports = {
  content: ["*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

**Add the Tailwind directives to your CSS *in src/input.css***

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

**Start the Tailwind CLI build process**
```
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```

**Start using Tailwind in your HTML**

> Add tailwindcss in html by adding css file in`<head>`

```
 <link rel="stylesheet" href="./output.css">
```
