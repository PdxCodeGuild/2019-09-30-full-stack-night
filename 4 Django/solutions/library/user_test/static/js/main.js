const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

$('.available').on('click', event => {
    // console.log(event.target.parentElement.parentElement.parentElement.id);
    const book_id = event.target.parentElement.parentElement.parentElement.id;

    url = `http://localhost:8000/catalog/checkout/${book_id}`;

    axios.post(url, {
        'book_id': book_id,
    },
        axios.defaults.xsrfCookieName = 'csrftoken',
        axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
    )
        .then(response => console.log(response))
        .catch(error => console.log(error))
})

$('.return').on('click', event => {
    // console.log(event.target.parentElement.parentElement.parentElement.id);
    const book_id = event.target.parentElement.parentElement.parentElement.id;

    url = `http://localhost:8000/catalog/checkin/${book_id}`;

    axios.post(url, {
        'book_id': book_id,
    },
        axios.defaults.xsrfCookieName = 'csrftoken',
        axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
    )
        .then(response => console.log(response))
        .catch(error => console.log(error))
})


$('.onloan').on('click', event => {
    // console.log(event.target.parentElement.parentElement.parentElement.id);
    const book_id = event.target.parentElement.parentElement.parentElement.id;

    url = `http://localhost:8000/catalog/reserved/${book_id}`;

    axios.post(url, {
        'book_id': book_id,
    },
        axios.defaults.xsrfCookieName = 'csrftoken',
        axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
    )
        .then(response => console.log(response))
        .catch(error => console.log(error))
})