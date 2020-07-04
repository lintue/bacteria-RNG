const merge = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
  mode: 'production',
  devtool: 'source map',
  entry: {
    loader: './src/Loader.js',
  },
  output: {
    path: __dirname+'/loader',
    filename: '[name].bundle.js',
  },
});
