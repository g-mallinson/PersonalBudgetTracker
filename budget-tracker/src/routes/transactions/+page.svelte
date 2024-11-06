<script lang="ts">
    import { onMount } from 'svelte';
    import axios from 'axios';

    let transactions = [];

    /**
     * Fetch transactions from the API on component mount and store them 
     * in the transactions variable.
     */
    onMount(async () => {
        const response = await axios.get('http://localhost:8000/transactions');
        transactions = response.data;

        // Set the date input value to today's date by default
        const today = new Date();
        date = today.toISOString().split('T')[0];
    });

    // Define variables to store form input values
    let date = '';
    let description = '';
    let category = '';
    let amount = '';
    let transaction_type = '';

    /**
     * Send a POST request to the API to add a new transaction.
     */
    const addTransaction = async () => {
        await axios.post('http://localhost:8000/transactions/', {
            date,
            description,
            category,
            amount: parseFloat(amount),
            transaction_type
        });

        // Refresh the transactions array by fetching the updated list from API
        const response = await axios.get('http://localhost:8000/transactions/');
        transactions = response.data;
        // Clear the form input values
        date = new Date().toISOString().split('T')[0]; // Reset to current date
        description = '';
        category = '';
        amount = '';
        transaction_type = '';
    };

    /**
     * Formats a number as a currency string.
     * 
     * @param {number} value - The number to format.
     * @returns {string} The formatted currency string.
     */
    function formatCurrency(value: number): string {
        return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);
    }
</script>

<h1 class="text-4xl font-bold mb-8 text-center text-gray-800">Transactions</h1>

<div class="flex justify-center">
    <div class="w-auto max-w-4xl px-4">
        <div class="overflow-x-auto">
            <table class="min-w-full bg-white shadow-lg rounded-lg overflow-hidden">
                <thead class="bg-indigo-600 text-white">
                    <tr>
                        <th class="py-3 px-4">Date</th>
                        <th class="py-3 px-4">Description</th>
                        <th class="py-3 px-4">Category</th>
                        <th class="py-3 px-4 text-right">Amount</th>
                        <th class="py-3 px-4">Transaction Type</th>
                    </tr>
                </thead>
                <tbody>
                    {#each transactions as transaction}
                        <tr class="even:bg-gray-100 odd:bg-white">
                            <td class="py-3 px-4 border-b">{transaction.date}</td>
                            <td class="py-3 px-4 border-b">{transaction.description}</td>
                            <td class="py-3 px-4 border-b">{transaction.category}</td>
                            <td class="py-3 px-4 border-b text-right">{formatCurrency(transaction.amount)}</td>
                            <td class="py-3 px-4 border-b">{transaction.transaction_type}</td>
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>
    </div>
</div>

<h2 class="text-3xl font-bold mt-12 mb-6 text-center text-gray-800">Add Transaction</h2>
<form on:submit|preventDefault={addTransaction} class="max-w-lg mx-auto space-y-6 bg-white p-8 rounded-lg shadow-lg">
    <label class="block">
        <span class="text-gray-700">Date:</span>
        <input type="date" bind:value={date} required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50 focus:ring-indigo-300">
    </label>
    <label class="block">
        <span class="text-gray-700">Description:</span>
        <input type="text" bind:value={description} required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50 focus:ring-indigo-300">
    </label>
    <label class="block">
        <span class="text-gray-700">Category:</span>
        <input type="text" bind:value={category} required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50 focus:ring-indigo-300">
    </label>
    <label class="block">
        <span class="text-gray-700">Amount:</span>
        <input type="number" step="0.01" bind:value={amount} required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50 focus:ring-indigo-300">
    </label>
    <label class="block">
        <span class="text-gray-700">Transaction Type:</span>
        <select bind:value={transaction_type} required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50 focus:ring-indigo-300">
            <option value="income">Income</option>
            <option value="expense">Expense</option>
        </select>
    </label>
    <button type="submit" class="w-full py-2 px-4 bg-indigo-600 text-black rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring focus:ring-opacity-50 focus:ring-indigo-300">Add Transaction</button>
</form>
