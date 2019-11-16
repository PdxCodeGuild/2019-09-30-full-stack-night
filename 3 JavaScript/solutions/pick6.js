function generateTicket() {
    low = 1;
    high = 99;
    const ticket = [];
    for (let i = 0; i < 6; i++)
        ticket.push(Math.floor(Math.random() * (1 + high - low)) + low);
    return ticket;
}


function compareTickets(winner, ticket) {
    let matches = 0;
    winner.forEach(function (value, index) {
        if (value == ticket[index])
            matches++;
    })
    return matches;
}


function main() {
    const prizes = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000,
    }
    
    
    let matches = 0;
    let winnings = 0;
    let expenses = 0;
    let iter = 0;
    const MAX_ITER = 99999;
    let ticket = [];


    const winner = generateTicket();


    while (iter <= MAX_ITER) {
        expenses += 2;
        ticket = generateTicket();

        matches = compareTickets(winner, ticket);

        winnings += prizes[matches];
        iter++;
    }


    console.log(`\nwinnings: ${winnings}\nexpenses: ${expenses}\nroi: ${(winnings - expenses) / expenses}\n`)
}

main()