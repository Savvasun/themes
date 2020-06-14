![Preview of the Windows Terminal Themes](https://github.com/atomcorp/themes/raw/master/app/public/preview-v3.png)

# Windows Terminal Themes

Preview and copy themes for the new [Windows Terminal](https://github.com/microsoft/terminal).

Use the project at [https://atomcorp.github.io/themes/](https://atomcorp.github.io/themes/)

## How to use the themes

This site let's you preview and then copy a theme you like (or download a json file with all of them).

The [official docs for Windows Terminal](https://github.com/microsoft/terminal/blob/master/doc/user-docs/UsingJsonSettings.md) seem to very thoroughly explain how to change the settings, but essentially:

* open Windows Terminal settings
* add your chosen theme(s) to `schemes`
* in `profiles`, find the shell you're using (eg cmd, powershell, ubuntu) and replace `colorScheme` with the name of the theme
* 🥳

## Contribute a theme

Ideally for the ecosystem new themes should be proposed to [iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) (where most of these themes come from), then everyone can benefit.

If not, new themes can be add added with a pull request. Just add them to the list in `app/src/custom-colour-schemes.json`. You shouldn't need to run anything. If you'd like to receive credit, or know who should, please add it to this README when submitting.

## Credits

* The OneDark theme was created by [azrikahar](https://github.com/azrikahar)
* The DraculaPlus, Material Darker and OneStar theme was created by [jos3s](https://github.com/jos3s)
* Monokai Cmder by [vdurante](https://github.com/vdurante/windows-terminal-monokai-cmder)

## Running

Install using `yarn` and run using `yarn start`, this should start both the React app and Express server.

You can run all the tests with `yarn test:dev`.

E2E tests are run with [cypress](https://www.cypress.io/). You can use `yarn cy:open` to open and develop using the Dashboard and run test suite with `yarn cy:run`. There's a few unit test using Jest that you can develop using `yarn unit:watch`.

There's CI with CircleCI and there's visual regression tests with Percy to.

### Compiling the themes

The json list is generated from another repo, [github.com/atomcorp/terminal-api](https://github.com/atomcorp/terminal-api). It merges all the schemes found in the [iTerm2-Color-Schemes/windowsterminal](https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/windowsterminal) using the GitHub API, then combines it with `src/custom-colour-schemes.json` in this repo. It runs on a server with a daily cron job.

## Todo

* [x] a way to share themes
* [x] testing with [cypress](https://www.cypress.io/)
* [x] automating the compilation step
* [x] improve responsiveness
* [x] add a codeblock view
* [x] nicer UI
* [x] create monorepo with [terminal-api](https://github.com/atomcorp/terminal-api)
* [ ] [add theme credits into app](#Progress)
* [ ] use canvas for rendering the colour test
* [ ] code refactor/tidy (it's gotten so ugly 😭)

## Notes

* Most themes are copied from [iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) so huge thanks and credit to them and all the theme designers
* aim is to be simple and accessible, please let me know any accessibility problems!
* this project is based around: React (create-react-app), TypeScript, Github Pages, immer and CSS Grid
* the following projects were really useful [clipboard-polyfill](https://github.com/lgarron/clipboard-polyfill), [resize-observer-polyfill](https://github.com/que-etc/resize-observer-polyfill), [file-saver](https://github.com/eligrey/FileSaver.js) and [get-contrast](https://github.com/johno/get-contrast) and (StylishThemes/GitHub-Dark)[https://github.com/StylishThemes/GitHub-Dark] for helping with dark mode colours and styling. Thanks!
* Icons are all [Material Design](https://material.io/resources/icons/?style=baseline), except GitHub's mark which is from (GitHub Primer)(https://primer.style/octicons/)
* Terminal logo is made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
* Indispensable logo animation help from https://codepen.io/NickNoordijk/pen/VLvxLE?editors=1010 & https://www.digitalocean.com/community/tutorials/svg-linear-gradients

## Progress

* The credits system is actually coming along! [Here is the issue with the discussion](https://github.com/atomcorp/themes/issues/8).
