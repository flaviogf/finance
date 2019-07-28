const webpack = require('webpack')
const path = require('path')
const CopyPlugin = require('copy-webpack-plugin')

module.exports = {
    mode: process.env.NODE_ENV,
    entry: path.join(__dirname, 'static', 'src', 'index.js'),
    plugins: [
        new CopyPlugin([{
            from: 'static/src/assets/images/**/*',
            to: '[name].[ext]',
            toType: 'template',
        }]),
    ],
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
        }, {
            test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
            loader: 'file-loader',
            options: {
                name: '[name].[ext]'
            }
        }]
    }
}