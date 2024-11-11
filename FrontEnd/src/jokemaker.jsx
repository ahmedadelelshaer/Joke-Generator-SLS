// JokeGenerator.js
import React, { useState } from 'react';
import axios from 'axios';
import './JokeGenerator.css';

const JokeGenerator = () => {
  const [joke, setJoke] = useState([]);

  const fetchJoke = async () => {
    try {
      // Replace this URL with your API Gateway endpoint
      
      
      const response = await axios.get('https://fp6ik9qmoc.execute-api.us-east-1.amazonaws.com/Prod/joke/');
      setJoke('')
      setJoke(prev=>[...prev,response.data.joke]);
    } catch (error) {
      setJoke('Sorry, failed to fetch a joke.');
    }
  };

  return (
    <div className="joke-container">
      <h1>Joke Generator</h1>
      <p className="joke-text">{joke}</p>
      <button onClick={fetchJoke} className="joke-button">Get a Joke</button>
    </div>
  );
};

export default JokeGenerator;
