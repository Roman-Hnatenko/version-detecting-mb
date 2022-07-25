const express = require("express");
const app = express();


const params = process.argv.slice(2);
const folderPath = params[0];
const mainFileName = params[1];

app.use(express.static(folderPath));
app.listen(3000, () => {
  console.log("Application started and Listening on port 3000");
});

app.get("/", (req, res) => {
  res.sendFile(folderPath + "/" + mainFileName);
});