module.exports = function (grunt) {

    var webpackConfig = require("./webpack.config");

    "use strict";

    grunt.initConfig({
        webpack: {
            dev: webpackConfig,
            prod: Object.assign(webpackConfig, {mode: "production"})
        },
        clean: {
            target: "shared/static/shared/js/lib"
        },
        copy: {
            lib: {
                files: [
                {
                    expand: true,
                    cwd: "node_modules/infusion/dist",
                    src: "**",
                    dest: "shared/static/shared/js/lib/infusion/dist"
                },
                {
                    expand: true,
                    cwd: "node_modules/infusion/src",
                    src: "**",
                    dest: "shared/static/shared/js/lib/infusion/src"
                }]
            }
        }
    })


    // Load the plugin(s):

    grunt.loadNpmTasks("grunt-contrib-copy");
    grunt.loadNpmTasks("grunt-contrib-clean");
    grunt.loadNpmTasks("grunt-webpack");
    
}