<script lang="ts">
  import { onMount } from 'svelte';
  import { marked } from 'marked';
  import { register } from '@tauri-apps/api/globalShortcut';

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

  onMount(() => {
    // Register a global shortcut
    register('CmdOrCtrl+Shift+Alt+G', async () => {
      console.log('Shortcut pressed');
    }).then(() => {
      console.log('Shortcut registered');
    }).catch((e) => {
      console.error('Failed to register shortcut', e);
    });
  });
</script>

<main class="max-w-2xl mx-auto p-4">
    <h1 class="text-8xl font-bold mb-4">DeskGPT</h1>
    <h3 class="text-xs font-semibold mb-2">ChatGPT 4o</h3>
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
