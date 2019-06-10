module.exports = function (api) {
  api.cache(true);

  const presets = [];
  const plugins = ["@babel/plugin-proposal-class-properties"];

  return {
    presets,
    plugins
  };
}
