var path = require('path');
var webpack = require('webpack');

var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    cache: true,
    entry: path.join(__dirname, 'app', 'js', 'app'),
    output: {
        path: path.join(__dirname, 'static'),
        publicPath: 'static/',
        filename: '[name].js',
        chunkFileName: '[chunkhash].js'
    },
    module: {
        loaders: [{
            test: /\.js$/,
            loader: '6to5-loader',
            exclude: /node_modules/
        }, {
            test: /\.(html|hbs)$/,
            loader:  'handlebars-loader?helperDirs[]='+__dirname+'/app/js/helpers'
        }]
    },
    resolve: {
        alias: {
            marionette: 'backbone.marionette',
            bootstrap: 'bootstrap-sass',
            utils: 'utils/utils',
            __templates__: __dirname + '/app/templates'
        }
    }, 
    plugins: [
        new HtmlWebpackPlugin({
            template: path.join('app/index.html')
        }), 
        new webpack.ProvidePlugin({
            jQuery: 'jquery',
            $: 'jquery'
        })
    ]
};