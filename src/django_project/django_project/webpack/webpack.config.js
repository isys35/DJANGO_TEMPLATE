const path = require('path');

module.exports = {
  entry: {
    index: './src/index.js',
    app: './src/app.js',
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
    clean: true,
  },
  module: {
    rules: [
      { //https://webpack.js.org/loaders/css-loader/
        test: /\.css$/,
        use: ["style-loader"]
      },
      { //https://webpack.js.org/loaders/css-loader/
        test: /\.css$/,
        loader: "css-loader",
        options: {
          url: false,
        }
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
        loader: 'file-loader',
        options: {
          outputPath: 'images',
          name: '[name].[ext]'
        },
      },
    ],
  },
};