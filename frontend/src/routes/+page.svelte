<script>
    import Button from '../components/Button.svelte';
    let count = 0;

    function handleClick() {
        count += 1;
    }

    $: {
        console.log(`The count is ${count}`);
    }

    $: if(count > 10) {
        alert(`Count is dangerously high!`);
        count = 0;
    }
</script>

<h1>Welcome to SvelteKit Demo</h1>

<Button />
<button on:click={handleClick}>Another Sample Button</button>

<style>
    button {
        background-color: red;
        color: white;
        padding: 10px;
        border-radius: 5px;
        border: none;
    }
</style>
