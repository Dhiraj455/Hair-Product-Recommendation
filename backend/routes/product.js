const express = require("express");
const router = express.Router();
const productController = require("../controllers/product");
const authentication = require("../middlewares/Auth");

router.post("/addProduct", productController.addProduct);

router.get("/getProducts", productController.getProducts);

module.exports = router;
