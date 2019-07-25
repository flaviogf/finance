const webpack = require('webpack')
const path = require('path')

module.exports = {
    mode: 'development',
    entry: path.join(__dirname, 'src', 'index.js'),
    output: {
        filename: 'app.min.js'
    },
    module: {
        rules: [{
            test: /\.s?[ac]ss$/,
            loaders: [
                'style-loader',
                'css-loader',
                'sass-loader'
            ]
        }]
    }
}