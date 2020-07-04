const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
  output: {
    path: __dirname+'/build',
    filename: '[name].bundle.js',
  },
  plugins: [
    new CleanWebpackPlugin(),
  ],
  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
      {
        test: /\.s[ac]ss$/,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader',
        ],
      },
      {
        test: /\.css$/i,
        use: [
          'style-loader',
          'css-loader'],
      },
      {
				test: /\.(png|gif|svg)$/,
				loader: 'url-loader',
			},
      {
        test: /\.txt$/i,
        use: 'raw-loader',
      },
      {
				test   : /\.(ttf|eot|woff(2)?)(\?[a-z0-9]+)?$/,
				loader : 'file-loader?name=../build-fonts/[name].[ext]',
			},
    ],
  },
};
