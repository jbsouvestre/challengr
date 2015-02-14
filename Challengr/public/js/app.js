import { history } from 'backbone';
import { Application } from 'marionette';
import Layout from './commons/layout';
import Router from './routes/router';
import Controller from './routes/controller';
import Session from './lib/Session';
import 'bootstrap';
import $ from 'jquery';

const HistoryOptions = {
    pushState: true
};

let App = new Application({
    regions: {
        AppRegion: '#app'
    }
});

App.addInitializer(() => {
    App.AppRegion.show(Layout);
    
    App.Router = new Router({
        controller: new Controller()
    });
    
    
    history.start(HistoryOptions);


    $(document).on('click', 'a:not([data-bypass])', (e) => {
        e.preventDefault();
        App.Router.navigate($(e.target).attr('href'), {
            trigger: true
        });
    });
});

App.start();

/*for debug*/
window.App = App;

window.jQuery = $;

console.log(Session.fetch());

export default App;
