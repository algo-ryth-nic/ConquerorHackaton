# DERMA 360
Frontend for Derma360 

## Setup
In order to locally setup the frontend, you'll need to create a firebase project.
For more information, you can check [docs](https://firebase.google.com/docs/auth/web/start)

Once you have a firebase project setup and a authentication enabled, create a `.env` file in the 
root level of the `frontend` directory.
The .env file should contain all the firebase related creds prefixed with `VITE_`

For example,
```env
VITE_API_KEY=<FIREBASE_API_KEY>
...
```

