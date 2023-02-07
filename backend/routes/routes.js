const express = require("express");
const router = express.Router();
const { api_version } = require("../config/config");

/**
 * @desc Opens the api documentation page
 * @route GET /movie-recommendation-system/api-version
 * @access Public
 **/

router.route("/api-version").get(async (req, res) => {
	res.json({ "API Version": api_version, "Status": res.statusCode });
});



module.exports = router;
