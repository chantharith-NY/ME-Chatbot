import { Injectable } from '@nestjs/common';
import axios from 'axios';
import axiosRetry from 'axios-retry';

@Injectable()
export class ChatbotService {
  private AI_MODEL_URL = 'http://localhost:5000/chat'; // AI model's API

  constructor() {
    // Configure axios to retry failed requests
    axiosRetry(axios, { retries: 3, retryDelay: axiosRetry.exponentialDelay });
  }

  async getResponse(message: string): Promise<string> {
    try {
      const response = await axios.post(this.AI_MODEL_URL, { message }, { timeout: 5000 });
      return response.data.response;  // Extract chatbot's response
    } catch (error) {
      console.error('Error communicating with AI model:', {
        message: error.message,
        stack: error.stack,
        config: error.config,
        response: error.response ? {
          status: error.response.status,
          data: error.response.data,
        } : null,
      });
      return 'Sorry, there was an issue connecting to the AI chatbot.';
    }
  }
}