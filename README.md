<h1 align="center">EasyCare monorepo</h1>

<p align="center">
  <a href="#setup"><strong>Setup</strong></a> |
  <a href="#tech-stack"><strong>Tech Stack</strong></a> |
</p>
<p align="center">
  <a href="https://next-fast-turbo.mintlify.app/">
    <img src="https://img.shields.io/badge/Read%20the%20Documentation-8A2BE2" alt="Documentation" />
  </a>
</p>
<br/>

## Setup

### Install Node version v20.18.0
I recommend to install it using [nvm](https://github.com/nvm-sh/nvm)
`nvm install v20.18.0`
`nvm alias default v20.18.0`
To activate the shell type `nvm use default`

### Install python (see version in `pyproject.toml`).
    * I recommend installing it via pyenv. [Follow the official documentation for installing pyenv on your system](https://github.com/pyenv/pyenv)
    * Then install the python version
        * `pyenv install 3.11.10`
    * Optional: Set global python version to the one you installed
        * `pyenv global 3.11.10`
### Install *poetry* globally 
`pip install poetry`

### Install pnpm
`npm install -g pnpm`

### Install dependencies
`pnpm install`

### Turbo setup
From the project root, run the command:
`npx turbo login`

Link your Turborepo to your Remote Cache by running the following command from the root of your Turborepo: 
`npx turbo link`

### Run project
`turbo dev`

Note: If you encounter an error indicating that Turbo is not installed, run the following command to install it globally:

`npm install -g turbo`

### Test your new endpoints
You can now test your new endpoints using the FastAPI Swagger UI or by making requests to the API.

## Tech Stack

- [Next.js](https://nextjs.org/) – Frontend Framework
- [Tailwind](https://tailwindcss.com/) – CSS Framework
- [ShadCN UI](https://ui.shadcn.com/) – UI Components
- [FastAPI](https://fastapi.tiangolo.com/) – Python Backend
- [Mintlify](https://mintlify.com/) – Documentation
- [Supabase](https://supabase.com/) – Database
- [Turborepo](https://turbo.build/repo) – Monorepo
- [Vercel](https://vercel.com/) – deployments

## Git flow used
https://nvie.com/posts/a-successful-git-branching-model/
