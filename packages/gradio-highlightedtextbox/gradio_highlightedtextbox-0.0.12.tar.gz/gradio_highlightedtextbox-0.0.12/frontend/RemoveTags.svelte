<script lang="ts">
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher()
</script>
 
<button
    on:click={() => dispatch('clear')}
    title="Remove highlights"
    aria-roledescription="Remove highlights"
    aria-label="Remove highlights"
>
    <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="2 0 20 20"
    fill="none"
    stroke="white"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"><polyline points="20 6 9 17 4 12" /></svg
    >
</button>

<style>
	button {
		position: relative;
		cursor: pointer;
		padding: 5px;
		width: 22px;
		height: 22px;
        background-color: green;
	}
</style>