import sidradataquality.sdk.constants as const
from sidradataquality.sdk.log.logging import Logger

import great_expectations as gx
from great_expectations.render.renderer import ValidationResultsPageRenderer, ProfilingResultsPageRenderer, ExpectationSuitePageRenderer
from great_expectations.render.view import DefaultJinjaPageView

class ReportService():
    def __init__(self, spark):
        self.logger = Logger(spark, self.__class__.__name__)

    def render(self, validations_result):
        self.logger.debug(f"[Report Service][render] Render report from results")
        return DefaultJinjaPageView().render(ValidationResultsPageRenderer().render(validations_result))

    def render_with_custom_style(self, validations_result):
        self.logger.debug(f"[Report Service][apply_custom_css_style] Apply custom CSS style to report")
        html_content = self.render(validations_result)
        style_content = self._get_custom_style()
        return html_content.replace('<style></style>', f'<style>{style_content}</style>')
        
    def _get_custom_style(self):
        return '''
:root {
  --primary: #8672fa;
  --primary-hover: #9887fb;
  --secondary: #66e1e4;
  --secondary-hover: #57bfc2;
  --white: #ffffff;
  --black: #15212f;
  --gray: #e9ecf0;
  --danger: #cc3366;
}

body {
  color: var(--black);
}

/* NAVBAR */

.navbar {
  background: var(--white);
}

.navbar-brand {
  width: 150px;
  height: 50px;
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  background-image: url(data:image/png;base64,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);
}

.navbar-brand.h-100 {
  height: 50px !important;
}

.navbar-brand a {
  display: none;
}

.navbar-expand-md::before {
  position: absolute;
  content: "powered by";
  top: 2px;
  right: 0;
  width: 200px;
  height: auto;
  padding-left: 25px;
  font-size: 0.8em;
  z-index: 4;
  text-align: left;
  background: var(--white);
}

.navbar-expand-md::after {
  position: absolute;
  content: "";
  top: 20px;
  right: 0px;
  width: 200px;
  height: 40px;
  background: var(--white);
  background-image: url("https://great-expectations-web-assets.s3.us-east-2.amazonaws.com/logo-long.png?d=20221102T130030.199543Z");
  background-repeat: no-repeat;
  background-size: contain;
  z-index: 5;
}

/* BUTTONS */

.btn-primary {
  color: var(--white) !important;
  background-color: var(--primary);
  border-color: var(--primary);
  cursor: pointer;
}

.btn-primary:hover,
.btn-primary.active,
.btn-primary:active {
  background-color: var(--primary-hover) !important;
  border-color: var(--primary-hover) !important;
}

.btn-warning,
.btn-info,
.btn-secondary {
  background-color: var(--secondary);
  border-color: var(--secondary);
  color: var(--white) !important;
}

.btn-warning:hover,
.btn-warning.active,
.btn-warning:active,
.btn-info:hover,
.btn-info.active,
.btn-info:active,
.btn-secondary:hover,
.btn-secondary.active,
.btn-secondary:active {
  background-color: var(--secondary-hover) !important;
  border-color: var(--secondary-hover) !important;
  color: var(--white) !important;
}

.btn-primary:focus,
.btn-primary.focus,
.btn-info:focus,
.btn-primary:focus,
.btn-secondary:focus,
.btn-warning:focus {
  box-shadow: none !important;
}

/* TEXTS */

a {
  color: var(--primary) !important;
}

.alert-secondary {
  background-color: var(--gray) !important;
}

.text-danger {
  color: var(--danger) !important;
}

.table {
  color: var(--black) !important;
}

.alert a {
  word-break: break-word;
}

/* RESPONSIVE */

@media (width < 1500px) {
  .nav-item {
    padding-right: 10px !important;
    padding-left: 10px !important;
  }
  .nav-link {
    padding: 0.4rem 0.5rem;
  }
  .breadcrumb {
    font-size: 0.9em;
  }
}

@media (width < 1100px) {
  .navbar::before {
    top: 8px;
    width: 150px;
    padding-left: 20px;
    font-size: 0.7em;
  }
  .navbar::after {
    top: 25px;
    width: 150px;
  }
  .breadcrumb {
    font-size: 0.8em;
  }
}

@media (width < 950px) {
  .navbar::before {
    top: 11px;
    width: 120px;
    padding-left: 16px;
    font-size: 0.6em;
  }
  .navbar::after {
    top: 25px;
    width: 120px;
  }
}

@media (width < 875px) {
  .breadcrumb {
    font-size: 0.8em;
  }
}

@media (width < 800px) {
  .navbar-brand {
    width: 120px;
  }
  .breadcrumb {
    font-size: 0.7em;
  }
}

@media (prefers-color-scheme: dark) {
  body {
    color: #ffffff; /* Texto blanco o claro */
  }
  .breadcrumb-item.active {
    color: #ced4da;
  }
  .table {
    color: #ffffff !important;
  }
  .alert-secondary {
    color: #383d41;
    background-color: #e2e3e5 !important;
    border-color: #d6d8db;
  }
  .navbar {
    background: transparent;
  }
  .navbar-expand-md::after {
    display: none;
  }
  .navbar-expand-md::before {
    background: transparent;
  }
  .navbar-brand {
    background-image: url(data:image/png;base64,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);
  }
  .navbar::before {
    background-color: rgb(25, 29, 33);
    top: 5px;
    width: 210px;
    padding-left: 32px;
  }
  .navbar-brand a {
    background-color: rgb(25, 29, 33);
    display: inline-block;
    position: fixed;
    top: 18px;
    right: 0;
    width: 210px;
    height: 50px;
  }
  .navbar-brand a img {
    width: 100%;
  }
}
@media (prefers-color-scheme: dark) and (width < 1100px) {
  .navbar::before {
    top: 3px;
  }
}
@media (prefers-color-scheme: dark) and (width < 950px) {
  .navbar::before {
    top: 5px;
  }
}
        '''