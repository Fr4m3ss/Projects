// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
//import { getDatabase } from "firebase/database";
import { getFirestore } from "@firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBkdML8cWFlBRckkBZXO43rbNaxcM8nzoM",
  authDomain: "capstone-project-app.firebaseapp.com",
  projectId: "capstone-project-app",
  storageBucket: "capstone-project-app.appspot.com",
  messagingSenderId: "236670050787",
  appId: "1:236670050787:web:026967494b79972bb2c0d6"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
let db = getFirestore();
export { db };