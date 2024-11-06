<script lang="ts">
    import { onMount } from 'svelte';
    import axios from 'axios';

    let transactions = [];

    /* Fetch transactions from the API on component mount and store them 
     * in the transactions variable */
    onMount(async () => {
        const response = await axios.get('http://localhost:8000/transactions');
        transactions = response.data;
    });

    // Define variables to store form input values
    let date = '';
    let description = '';
    let category = '';
    let amount = '';
    let transaction_type = '';
    
    const addTransaction = async () => {
        // Send a POST request to the API to add a new transaction
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
        date = '';
        description = '';
        category = '';
        amount = '';
        transaction_type = '';
    };
</script>

<h1>Transactions</h1>

<table>
    <thead>
        <tr>
            <th>Date</th>
            <th>Description</th>
            <th>Category</th>
            <th>Amount</th>
            <th>Transaction Type</th>
        </tr>
    </thead>
    <!-- Loop through transactions array and display each transaction in a row -->
    <tbody>
        {#each transactions as transaction}
            <tr>
                <td>{transaction.date}</td>
                <td>{transaction.description}</td>
                <td>{transaction.category}</td>
                <td>{transaction.amount}</td>
                <td>{transaction.transaction_type}</td>
            </tr>
        {/each}
    </tbody>
</table>

<h2> Add Transaction </h2>

<form on:submit|preventDefault={addTransaction}>
    <label>
        Date:
        <input type="date" bind:value={date} required>
    </label>
    <label>
        Description:
        <input type="text" bind:value={description} required>
    </label>
    <label>
        Category:
        <select bind:value={category} required>
            <option value="salary">Salary</option>
            <option value="entertainment">Entertainment</option>
            <option value="food">Food</option>
            <option value="transport">Transport</option>
            <option value="utilities">Utilities</option>
            <option value="other">Other</option>
    </label>
    <label>
        Amount:
        <input type="number" step="0.01" bind:value={amount} required>
    </label>
    <label>
        Transaction Type:
        <select bind:value={transaction_type} required>
            <option value="income">Income</option>
            <option value="expense">Expense</option>
        </select>
    </label>
    <button type="submit">Add Transaction</button>
</form>

<style>
    table {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
    }

    th {
        background-color: #f2f2f2;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    label {
        display: block;
        margin-bottom: 8px;
    }
</style>
