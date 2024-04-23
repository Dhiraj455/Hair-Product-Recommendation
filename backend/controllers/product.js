const Product = require("../models/product")

module.exports.addProduct = async (req, res) => {
    const response = {
        success: false,
        message: "",
        errMessage: "",
        data: "",
    };
    try {
        const { name, price, quantity, image } = req.body;
        console.log(req.body);
        const product = new Product({
            name,
            price,
            quantity,
            image,
        });
        const savedProduct = await product.save();
        response.success = true;
        response.message = "Product added successfully";
        response.data = savedProduct;
        return res.status(200).json(response);
    } catch (err) {
        console.log(err);
        response.errMessage = "Error adding product";
        return res.status(500).json(response);
    }
}

module.exports.getProducts = async (req, res) => {
    const response = {
        success: false,
        message: "",
        errMessage: "",
        data: "",
    };
    try {
        const products = await Product.find();
        response.success = true;
        response.message = "Products fetched successfully";
        response.data = products;
        return res.status(200).json(response);
    } catch (err) {
        console.log(err);
        response.errMessage = "Error fetching products";
        return res.status(500).json(response);
    }
}