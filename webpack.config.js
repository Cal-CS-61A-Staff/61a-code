const webpack = require("webpack");

module.exports = {
    module: {
        noParse: /monaco-editor\/min\/vs\/loader\.js|jquery\.jsPlumb-1\.3\.10-all-min\.js/,
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            jquery: 'jquery',
        })
    ]
};
