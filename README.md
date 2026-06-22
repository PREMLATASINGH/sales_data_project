Vercel deployment

This project provides a simple Python serverless function for Vercel.

Deploy steps:

1. Install the Vercel CLI:

```
npm i -g vercel
```

2. Login and deploy:

```
vercel login
vercel --prod
```

API endpoint after deploy:

- `https://<your-deployment>.vercel.app/api/sales`
