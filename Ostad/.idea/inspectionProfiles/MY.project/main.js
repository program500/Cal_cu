document.addEventListener('DOMContentLoaded', function() {
    // Example: Add a simple alert on 'Add to Cart' button click
    document.querySelectorAll('.btn-primary').forEach(button => {
        button.addEventListener('click', function() {
            alert('Item added to cart!');
        });
    });
});

