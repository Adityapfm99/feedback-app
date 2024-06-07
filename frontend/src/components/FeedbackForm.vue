<template>
    <div class="feedback-form">
      <div class="rating-container">
        
        <p><strong>How would you rate your satisfaction with our product?</strong></p>
        <div class="stars">
          <span
            v-for="n in 5"
            :key="n"
            class="star"
            :class="{ selected: n <= score }"
            @click="setRating(n)"
          >
            &#9733;
          </span>
        </div>
        <div class="labels">
        <span><strong>Very dissatisfied</strong></span>
        <span><strong>Very satisfied</strong></span>
      </div>
        <button @click="submitFeedback">Submit</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        score: 0,
      };
    },
    methods: {
      setRating(n) {
        this.score = n;
      },
      async submitFeedback() {
        if (this.score === 0) {
          alert('Please select a rating.');
          return;
        }
        try {
          await axios.post('http://localhost:8000/feedback/', {
            rating: this.score,
          });
          alert('Feedback submitted!');
          this.score = 0; // Reset the score after submission
        } catch (error) {
          console.error('There was an error!', error);
          alert('An error occurred while submitting feedback.');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .feedback-form {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .rating-container {
    text-align: center;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 300px;
  }
  
  .stars {
    display: flex;
    justify-content: center;
    margin-bottom: 10px;
  }
  
  .star {
    font-size: 2em;
    cursor: pointer;
    color: #e0e0e0;
  }
  
  .star.selected {
    color: #ffd700;
  }
  
  .labels {
  display: flex;
  justify-content: space-between;
  font-size: 0.8em;
  color: #888;
}
  
  button {
    background-color: #6200ea;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 10px;
  }
  
  button:hover {
    background-color: #3700b3;
  }
  </style>
  