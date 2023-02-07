const mongoose = require("mongoose");
const Config = require("../config/config.js");

const userSchema = new mongoose.Schema({
	name: {
		type: String,
		required: [true, "Name is required"],
	},
	username: {
		type: String,
		required: [true, "Username is required"],
		unique: [true, "Username is already taken"],
	},
	email: {
		type: String,
		required: [true, "Email is required"],
		unique: [true, "Email is already in use"],
	},
	password: {
		type: String,
		required: [true, "Password is required"],
		minLength: [6, "Password must be 6 characters long!"],
		select: false,
	},
	movies: [
		{
			type: String,
		},
	],
});

const userModel = mongoose.model(Config.collection_names.User, userSchema);

module.exports = userModel;
