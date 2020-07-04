const merge = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
  mode: 'production',
  devtool: 'source map',
  entry: {
    main: './src/Main.js',
  },
});
