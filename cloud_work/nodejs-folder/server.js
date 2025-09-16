// const express = require("express")

// const PORT = 8082

// const app = express()

// app.get("/", (req, res) => {
//     res.send("Hello~ Have a nice day!")
// });

// app.listen(PORT);
// console.log("Server in running..")

const express = require('express');
const redis = require('redis');

const client = redis.createClient({
    url: 'redis://redis-server:6379'
});

async function start() {
    await client.connect();               // v4에서는 connect() 제공
    console.log('Redis connected');

    const app = express();
    app.get('/', async (req, res) => {
        let number = await client.get('number') || 0;
        res.send(`숫자가 1씩 올라갑니다. 숫자: ${number}`);
        await client.set('number', Number(number) + 1);
    });

    app.listen(8082, '0.0.0.0', () => {
        console.log('Server running on 8082');
    });
}

start().catch(console.error);