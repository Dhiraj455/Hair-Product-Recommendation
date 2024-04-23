const express = require("express");
const router = express.Router();
const cartController = require("../controllers/cart");
const authentication = require("../middlewares/Auth");

router.post("/addCart", authentication, cartController.addCart);

router.get("/getCart", cartController.getCart);

router.delete("/deleteCart/:id", cartController.deleteCart);

router.post("/buyCart", cartController.buyCart);

module.exports = router;
