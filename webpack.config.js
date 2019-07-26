const webpack = require('webpack')
const path = require('path')

module.exports = {
    mode: 'development',
    entry: path.join(__dirname, 'static', 'src', 'index.js'),
    output: {
        filename: 'app.min.js',
        path: path.join(__dirname, 'app', 'static')
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