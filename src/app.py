from flask import Flask, jsonify, request

app = Flask(__name__)

from productos import productsGC

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!!"})

@app.route('/productos')
def getProducts():
    return jsonify({"products": productsGC, "message": "Products's List"})

@app.route('/productos/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in productsGC if product['nombre'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"Producto": productsFound[0]})
    return jsonify({"message": "Producto no encontrado"})

@app.route('/productos', methods=['POST'])
def addProduct():
    new_product = {
        "nombre": request.json['name'],
        "precio": request.json['price'],
        "cantidad": request.json['quantity']
    }
    productsGC.append(new_product)
    return jsonify({"message": "producto agregado satisfactoriamente", "productos": productsGC})

@app.route('/productos/<string:product_name>', methods=['PUT'])
def edithProduct(product_name):
    productFound = [product for product in productsGC if product['nombre'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['nombre'] = request.json['name']
        productFound[0]['precio'] = request.json['price']
        productFound[0]['cantidad'] = request.json['quantity']
        return jsonify({
            "message": "Producto actualizado",
            "Producto": productFound[0]})
    return jsonify({"message": "Producto no encontrado"})

@app.route('/productos/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    delProductFount = [product for product in productsGC if product['nombre'] == product_name]
    if len(delProductFount) > 0:
        productsGC.remove(delProductFount[0])
        return jsonify({
            "message": "Producto eliminado",
            "product": productsGC})
    return jsonify({"message": "producto no encontrado"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=4000)