const express = require("express");
const app = express();
const cookieParser = require("cookie-parser");
const path = require("path");
const routes = require("./routes/routes");

if (process.env.NODE_ENV != "production") {
	//if not in production then set dotenv to load .env variables
	require("dotenv").config({ path: "backend/config/.env" });
}

//serve static assets if in production
if (process.env.NODE_ENV == "production") {
	app.use(express.static(path.join(__dirname, "../frontend/out")));

	app.get("*", (req, res) => {
		res.sendFile(path.join(__dirname, "../frontend/out/index.html"));
	});
}

//using middleware
app.use(express.json({ limit: "50mb" }));
app.use(express.urlencoded({ limit: "50mb", extended: true }));
app.use(cookieParser());

//using routes
app.use("/movie-recommendation-system", routes);

module.exports = app;
