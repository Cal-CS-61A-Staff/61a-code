const webpack = require("webpack");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");

module.exports = {
    module: {
        noParse: /monaco-editor\/min\/vs\/loader\.js|jquery\.jsPlumb-1\.3\.10-all-min\.js/,
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: "eslint-loader",
                options: {
                    emitError: false,
                    emitWarning: true,
                },
            },
        ],
    },
    plugins: [
        new CleanWebpackPlugin(),
        new webpack.DefinePlugin({
            ELECTRON: true,
            VERSION: "\"1.0.1\"",
        }),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            jquery: "jquery",
        }),
    ],
};
