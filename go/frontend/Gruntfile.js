module.exports = function(grunt) {

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-coffee');
    grunt.loadNpmTasks('grunt-karma');
    grunt.loadNpmTasks('grunt-ngmin');

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        coffee: {
            build: {
                expand: true,
                cwd: 'app',
                src: ['**/*.coffee'],
                dest: '../static/app',
                ext: '.js'
            }
        },
        jshint: {
            all: ['Gruntfile.js', 'app/**/*.js', '../static/app/**/*.js'],
            options: {
                eqeqeq: true,
                globals: {
                    angular: true
                }
            }
        },
        concat: {
            options: {
                banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - ' + '<%= grunt.template.today("yyyy-mm-dd") %>\n' + '<%= pkg.homepage ? " *  " + pkg.homepage + "\\n" : "" %>' + ' *  Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author %> | Licensed <%= pkg.license %>\n' + ' */\n'
            },
            src: {
                src: [
                        '../static/app/app.js',
                        '../static/app/app.router.js',
                        '../static/app/**/*.js'
                ],
                dest: '../static/build/<%= pkg.name %>.js'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> - v<%= pkg.version %> */\n'
            },
            build: {
                src: '../static/build/<%= pkg.name %>.js',
                dest: '../static/build/<%= pkg.name %>.min.js'
            }
        },
        watch: {
            src: {
                files: '<config:jshint.all>',
                tasks: ['jshint', 'concat', 'uglify']
                // options: {
                //   nospawn: true,
                // }
            }
        },
        karma: {
            unit: {
                configFile: 'karma.conf.js',
                singleRun: true
            }
        },
        ngmin: {
            src: {
                src: '<%= concat.src.dest %>',
                dest: '<%= concat.src.dest %>'
            }
        }
    });

    // Load the plugin that provides the "uglify" task.
    grunt.loadNpmTasks('grunt-contrib-uglify');

    // Default task(s).
    grunt.registerTask('default', ['coffee', 'jshint']);
    grunt.registerTask('scripts', ['coffee']);
    grunt.registerTask('build', ['coffee', 'jshint', 'concat', 'uglify']);
    grunt.registerTask('test', ['coffee', 'jshint', 'karma']);

};