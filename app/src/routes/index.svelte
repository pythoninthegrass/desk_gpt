<script lang="ts">
  import { onMount } from 'svelte';
  import { marked } from 'marked';

  type ChatMessage = {
    role: 'user' | 'assistant';
    content: string;
  };

  let message: string = '';
  let chatHistory: ChatMessage[] = [];

  async function sendMessage() {
    const response = await fetch('http://127.0.0.1:8000/api/chat/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message })
    });

    if (response.ok) {
      const data: { response: string } = await response.json();
      chatHistory = [
        ...chatHistory,
        { role: 'user', content: message },
        { role: 'assistant', content: marked(data.response) as string }
      ];
      message = '';
    } else {
      console.error('Failed to send message');
    }
  }
</script>

<main class="max-w-2xl mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Chat with GPT-4.0</h1>
    <div class="mb-4 space-y-2 chat-history">
        {#each chatHistory as chat (chat.content)}
            <div class="p-2 rounded {chat.role === 'user' ? 'bg-blue-100' : 'bg-green-100'}">
                <p class="font-semibold">{chat.role}:</p>
                {@html chat.content}
            </div>
        {/each}
    </div>
    <form class="chat-form" on:submit|preventDefault={sendMessage}>
        <input
            type="text"
            bind:value={message}
            placeholder="Type your message..."
            class="chat-input"
        />
        <button type="submit" class="chat-button">Send</button>
    </form>
</main>

<style>
/* See ./app/src/app.css */
</style>
