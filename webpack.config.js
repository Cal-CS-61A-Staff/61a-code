const webpack = require("webpack");

module.exports = {
    module: {
        noParse: /monaco-editor\/min\/vs\/loader\.js/,
        rules: [
            {
                test: /pytutor\.js/,
                use: "exports-loader?ExecutionVisualizer"
            }
        ]
        // rules: [{
        //     test: require.resolve('jquery'),
        //     use: [{
        //         loader: 'expose-loader',
        //         options: 'jQuery'
        //     }, {
        //         loader: 'expose-loader',
        //         options: '$'
        //     }]
        // }]

    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            jquery: 'jquery'
        })
    ]
};
