


## 🗂️ Organization Chart Structure

The organization chart is managed using the `public/hierarchy.json` file. This file defines the hierarchical structure of the organization in JSON format.

📄 **Example Entry**

```json
{
  "name": "Sridhar Ramaswamy",
  "title": "CEO",
  "type": "person",
  "children": [
    {
      "name": "Benoit Dageville",
      "title": "Co-founder - President of Products",
      "type": "person",
      "children": []
    }
  ]
}
```

🧩 **Entry Fields**

Each entry in the JSON file must include the following fields:

- name: The name of the individual or entity.
- title: Their role or position in the organization.
- type: The type of node (e.g. "person" or "account").
- children: An array of subordinate entries (can be empty).


🚀 **Making Changes**

To update the organization chart:

1. Edit the public/hierarchy.json file with your desired changes.
2. Commit the changes to the main branch.
3. Once pushed, a GitHub Action will automatically deploy to production.


## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
│   └── favicon.svg
├── src/
│   ├── layouts/
│   │   └── Layout.astro
│   └── pages/
│       └── index.astro
└── package.json


To learn more about the folder structure of an Astro project, refer to [our guide on project structure](https://docs.astro.build/en/basics/project-structure/).

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).
