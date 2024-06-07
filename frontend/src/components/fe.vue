<template>
    <div class="rating-container">
      <h2>How would you rate your satisfaction with our product?</h2>
      <div class="stars">
        <span
          v-for="n in 5"
          :key="n"
          :class="['star', { active: n <= rating }]"
          @click="setRating(n)"
        >
          ★
        </span>
      </div>
      <div class="rating-labels">
        <span>Very dissatisfied</span>
        <span>Very satisfied</span>
      </div>
      <button @click="submitFeedback">Submit</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        rating: null,
      };
    },
    methods: {
      setRating(rating) {
        this.rating = rating;
      },
      async submitFeedback() {
        if (this.rating === null) {
          alert('Please select a rating before submitting.');
          return;
        }
        try {
          await axios.post('http://localhost:8000/feedback/', {
            rating: this.rating,
          });
          alert('Feedback submitted!');
        } catch (error) {
          console.error('There was an error!', error);
          alert('An error occurred while submitting feedback.');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .rating-container {
    text-align: center;
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .stars {
    display: flex;
    justify-content: center;
    margin: 20px 0;
  }
  
  .star {
    font-size: 2rem;
    cursor: pointer;
    color: #ddd;
    transition: color 0.3s;
  }
  
  .star.active {
    color: #ffcc00;
  }
  
  .rating-labels {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
  }
  
  button {
    background-color: #6200ea;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #3700b3;
  }
  </style>
  