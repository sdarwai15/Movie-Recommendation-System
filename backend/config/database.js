const mongoose = require("mongoose");
mongoose.set("strictQuery", true);

exports.connectDatabase = () => {
	mongoose
		.connect(process.env.MONGO_URI)
		.then((conn) => {
			console.log(
				`Connected to database! on ${conn.connection.host} at port ${conn.connection.port}`
			);
		})
		.catch((err) => {
			console.log("Connection to database failed due to foll. error: ");
			console.log(err);
		});
};
