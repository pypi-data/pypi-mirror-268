Changelog
=========

.. Each release has its own section structured as follows:
    Title: version (release date)
    Short prose summary of most important changes.
    List of changes with who made them and a link to the PR.

Unreleased
----------

.. Add your changes here, highlighting any user facing changes. E.g:
.. "* `@gh-user`_ did foo to bar in :pr:`9999`. This enables baz."

24.4.1 (2024-04-19)
-------------------

This release contains a large generalisation of the CSET workflow, allowing use
of templating to use the same recipe for multiple variables. It also adds
cycling to the workflow, so a long workflow can be efficiently processed in
parallel.

* `@jfrost-mo`_ added GitHub Issue and Pull Request templates, and a detailed
  contribution checklist to the documentation in :pr:`465`
* `@jfrost-mo`_ added a changelog in :pr:`468`
* `@jfrost-mo`_ documented the ``category`` recipe key in :pr:`499`
* `@jfrost-mo`_ renamed the ``steps`` and ``post-steps`` keys to ``parallel``
  and ``collate`` in :pr:`484`. This makes them more meaningful, but is a
  **breaking change**.
* `@daflack`_ added some generic arithmetic operators in :pr:`452`
* `@jfrost-mo`_ made the log output of the read operator nicer in :pr:`461`
* `@jfrost-mo`_ added links to share feedback to the output page in :pr:`442`
* `@jfrost-mo`_ documented some common errors in :pr:`443`
* `@jfrost-mo`_ documented the deprecation policy in :pr:`444`
* `@jfrost-mo`_ fixed an iris deprecation warning for save_split_attrs in :pr:`459`
* `@jfrost-mo`_ added LFRic specific recipes in :pr:`462`. This allows CSET to
  read in structured LFRic data.
* `@jfrost-mo`_ fixed a memory leak when plotting in :pr:`482`
* `@jfrost-mo`_ included the recipe title in the plot title, giving more context
  to the output. This was :pr:`462`
* `@Sylviabohnenstengel`_ added the capability to loop over model levels in :pr:`441`
* `@Sylviabohnenstengel`_ and `@jfrost-mo`_ renamed and better linked up the
  :doc:`/contributing/index` in :pr:`434` and :pr:`435`
* `@jfrost-mo`_ updated the documentation Actions workflow to make it simpler and
  faster in :pr:`449`
* `@jfrost-mo`_ added a cycling to the cylc workflow so recipes can be run in
  parallel across multiple nodes. This was :pr:`395`
* `@jfrost-mo`_ added looping inside an include file for generalisation in :pr:`387`
* `@jwarner8`_ added a basic regridding operator in :pr:`405`
* `@jfrost-mo`_ made conda-lock update PRs use a GitHub App in :pr:`415`
* `@Sylviabohnenstengel`_ retitled code and tooling setup page in :pr:`433`
* `@Sylviabohnenstengel`_ updated git terminology in :pr:`436`
* `@jfrost-mo`_ added sequential plot display with unified postage stamp plots in :pr:`379`
* `@JorgeBornemann`_ fixed IFS in build conda in :pr:`447`
* `@jfrost-mo`_ added a licence header to convection tests in :pr:`450`

.. _@JorgeBornemann: https://github.com/JorgeBornemann
.. _@jwarner8: https://github.com/jwarner8

24.2.1 (2024-03-04)
-------------------

A small bug fix release containing several fixes that ensure portability on
Australia's NCI system.

* Graceful error when graphing without xdg-open by `@jfrost-mo`_ in :pr:`394`
* Docs update by `@jfrost-mo`_ in :pr:`392`
* Update workflow conda lockfiles automatically by `@jfrost-mo`_ in :pr:`410`
* Handle ``LD_LIBRARY_PATH`` being unset by `@jfrost-mo`_ in :pr:`404`

24.2.0 (2024-02-13)
-------------------

This release open sources the cylc workflow, allowing for much easier running of
CSET over large datasets. It also includes support for parametrising recipes to
allow a single recipe to work for many cases.

* Open source workflow by `@jfrost-mo`_ in :pr:`247`
* CAPE ratio diagnostic by `@daflack`_ in :pr:`325`
* CAPE ratio rose edit tweak by `@daflack`_ in :pr:`332`
* Minor bug fix to cape ratio documentation by `@daflack`_ in :pr:`336`
* Use cached conda environment for CI by `@jfrost-mo`_ in :pr:`351`
* Single cube read operator by `@jfrost-mo`_ in :pr:`323`
* Hash updated config ensuring unique branch by `@jfrost-mo`_ in :pr:`350`
* Add filter_multiple_cubes operator by `@jfrost-mo`_ in :pr:`362`
* Test exception for invalid output directory by `@jfrost-mo`_ in :pr:`364`
* Test no constraints given to filter_multiple_cubes by `@jfrost-mo`_ in :pr:`363`
* Update workflow-installation.rst by `@Sylviabohnenstengel`_ in :pr:`365`
* Recipe parametrisation by `@jfrost-mo`_ in :pr:`337`
* Fix crash when running recipe from env var by `@jfrost-mo`_ in :pr:`384`

0.5.0 (2023-11-24)
------------------

Small update featuring some better looking plots (though still a
work-in-progress, see :issue:`240`) and a documentation fix.

* Bump version to 0.5.0 by `@jfrost-mo`_ in :pr:`278`
* Improve contour plot by `@jfrost-mo`_ in :pr:`282`

0.4.0 (2023-11-23)
------------------

Containing many months of work, this release contains many usability
improvements, new generic operators, and a big change to the output, where it is
now generated as handily viewable HTML pages.

* Update version to 0.4.0 by `@jfrost-mo`_ in :pr:`180`
* Postage stamp plots by `@jfrost-mo`_ in :pr:`160`
* Add collapse operator with corresponding yaml file and changes  by `@Sylviabohnenstengel`_ in :pr:`168`
* Make plot.contour_plot and write.write_cube_to_nc return a cube by `@jfrost-mo`_ in :pr:`183`
* Postage stamp plot fix by `@jfrost-mo`_ in :pr:`181`
* Document collapse operator by `@jfrost-mo`_ in :pr:`185`
* Refactor tests to use PyTest helpers by `@jfrost-mo`_ in :pr:`177`
* Document installing CSET into its own environment by `@jfrost-mo`_ in :pr:`198`
* Update README.md by `@Sylviabohnenstengel`_ in :pr:`206`
* Use hash of updated lock files in branch name by `@jfrost-mo`_ in :pr:`201`
* Add note on updating a cloned repository by `@jfrost-mo`_ in :pr:`190`
* Skip build-docs on push to main by `@jfrost-mo`_ in :pr:`200`
* Python 3.12 support by `@jfrost-mo`_ in :pr:`202`
* Update README.md by `@Sylviabohnenstengel`_ in :pr:`225`
* Update README.md by `@Sylviabohnenstengel`_ in :pr:`226`
* Update why-cset.rst by `@Sylviabohnenstengel`_ in :pr:`227`
* Fix globbing for lock file hashing by `@jfrost-mo`_ in :pr:`229`
* Update index.rst by `@Sylviabohnenstengel`_ in :pr:`228`
* Update index.rst by `@Sylviabohnenstengel`_ in :pr:`230`
* Use static branch name while updating lock files by `@jfrost-mo`_ in :pr:`245`
* Swap out flake8 for Ruff by `@jfrost-mo`_ in :pr:`218`
* Including aggregate operator. by `@Sylviabohnenstengel`_ in :pr:`241`
* Fix filter operator for filtering cube by `@daflack`_ in :pr:`258`
* Fix pre-commit mangling test data by `@jfrost-mo`_ in :pr:`273`
* Improve tutorials by `@jfrost-mo`_ in :pr:`209`
* Model level constraint operator by `@Sylviabohnenstengel`_ in :pr:`272`
* Plot generation improvements by `@jfrost-mo`_ in :pr:`274`

.. _@daflack: https://github.com/daflack

0.3.0 (2023-08-02)
------------------

This release contains some major changes to the user experience. This includes
many of the CLI commands changing names, and the :doc:`/index` being completely
restructured. Hopefully this should be the last major reshuffle of the user
experience, as we are getting closers to being feature complete for our MVP.

Other highlights include the addition of the :ref:`cset-graph-command` command
for visualising recipes, and the :ref:`cset-cookbook-command` command for
dumping the built in recipes to disk.

* Operator runner improvements by `@jfrost-mo`_ in :pr:`128`
* Add codespell pre-commit hook by `@jfrost-mo`_ in :pr:`135`
* Add graph command to visualise recipe files by `@jfrost-mo`_ in :pr:`136`
* Pin version of tox used in environment by `@jfrost-mo`_ in :pr:`142`
* Increase version number by `@jfrost-mo`_ in :pr:`124`
* Update description of CSET by `@jfrost-mo`_ in :pr:`141`
* Refactoring by `@jfrost-mo`_ in :pr:`144`
* Rename run command to bake by `@jfrost-mo`_ in :pr:`143`
* Add command to create recipes on disk by `@jfrost-mo`_ in :pr:`140`
* Documentation restructure by `@jfrost-mo`_ in :pr:`151`
* Add version command by `@jfrost-mo`_ in :pr:`156`
* General cleanup by `@jfrost-mo`_ in :pr:`158`
* Remove Python 3.8 support by `@jfrost-mo`_ in :pr:`173`
* Fix install instructions in docs by `@jfrost-mo`_ in :pr:`176`
* Allow PR checks to be run manually by `@jfrost-mo`_ in :pr:`179`
* Ensemble ingestion with read operator by `@jfrost-mo`_ in :pr:`157`
* Update working practices link to point to contributing docs by `@jfrost-mo`_ in :pr:`175`

0.2.0 (2023-06-16)
------------------

Lots of good work in the release towards making the recipe format more usable.

* Update installation instructions to use conda and add missing operators to documentation by `@jfrost-mo`_ in :pr:`94`
* Update index.rst by `@Sylviabohnenstengel`_ in :pr:`95`
* Improve installation instructions by `@jfrost-mo`_ in :pr:`97`
* Use speedy libmamba when resolving conda environments by `@jfrost-mo`_ in :pr:`105`
* Add documentation on rational by `@jfrost-mo`_ in :pr:`102`
* Relax version requirement for sphinx by `@jfrost-mo`_ in :pr:`108`
* Run PR checks on push to main by `@jfrost-mo`_ in :pr:`109`
* Move to YAML recipe format by `@jfrost-mo`_ in :pr:`119`
* Lock pre-commit config to specific SHA by `@jfrost-mo`_ in :pr:`118`
* Use recipes from environment variable by `@jfrost-mo`_ in :pr:`122`

.. _@Sylviabohnenstengel: https://github.com/Sylviabohnenstengel

0.1.0 (2023-04-24)
------------------

The first release of CSET! 🎉 This release contains basic operators to do
reading, writing, filtering, and plotting of data. It is however still quite
limited in each of them, and still doesn't promise much in the way of API
stability, with things undoubtedly going to undergo significant change in the
near future.

This release also serves as a basis for packaging CSET out into the wider world;
packages will be released on `PyPI <https://pypi.org/project/CSET/>`_, and
`conda-forge <https://anaconda.org/conda-forge/cset>`_.

* Re-enable testing on python 3.11 by `@jfrost-mo`_ in :pr:`61`
* Operator runner improvements by `@jfrost-mo`_ in :pr:`56`
* Move METplus tasks out of command line repository by `@jfrost-mo`_ in :pr:`76`
* Remove extra punctuation from conda lock CI commit message by `@jfrost-mo`_ in :pr:`78`
* Measure test coverage by `@jfrost-mo`_ in :pr:`68`
* Improve test coverage by `@jfrost-mo`_ in :pr:`81`
* Fix link to Git tutorial by `@jfrost-mo`_ in :pr:`83`
* Fix description of a git tag by `@jfrost-mo`_ in :pr:`84`
* Add basic plotting capabilities by `@jfrost-mo`_ in :pr:`85`
* Make PR coverage reports edit last comment by `@jfrost-mo`_ in :pr:`92`
* Package on PyPI by `@jfrost-mo`_ in :pr:`90`

.. _@jfrost-mo: https://github.com/jfrost-mo
